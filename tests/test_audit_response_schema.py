"""Synthetic schema checks; these are not experimental observations."""

import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator


SCHEMA_PATH = Path(__file__).resolve().parents[1] / 'schemas' / 'audit_response.schema.json'


class AuditResponseSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema)

    def response(self, **overrides):
        return {
            'schema_version': '0.1.0',
            'artifact_id': 'synthetic_case_1',
            'assessment': 'scored',
            'suspicion_probability': 0.5,
            'primary_diagnosis': None,
            'proposed_fix': None,
            'limitations': 'Synthetic schema check, not empirical evidence.',
            **overrides,
        }

    def test_valid_artifact_identifiers(self):
        for value in ('a', 'Case-1_example', 'x' * 64):
            with self.subTest(value=value):
                self.validator.validate(self.response(artifact_id=value))

    def test_invalid_artifact_identifiers(self):
        for value in ('', 'x' * 65, 'example\n', 'example\r\n', 'with space',
                      '../private', 'nested/name', 'tab\tid', '\u00e9', None):
            with self.subTest(value=value):
                self.assertFalse(self.validator.is_valid(self.response(artifact_id=value)))

    def test_scored_probability_bounds(self):
        for value in (0, 0.5, 1):
            with self.subTest(value=value):
                self.validator.validate(self.response(suspicion_probability=value))
        for value in (-0.1, 1.1, None, True, '0.5'):
            with self.subTest(value=value):
                self.assertFalse(self.validator.is_valid(
                    self.response(suspicion_probability=value)))

    def test_abstention_requires_null_probability(self):
        self.validator.validate(self.response(assessment='abstain', suspicion_probability=None))
        self.assertFalse(self.validator.is_valid(self.response(assessment='abstain')))

    def test_unknown_fields_and_values_rejected(self):
        for change in ({'label': 'benign'}, {'assessment': 'unknown'},
                       {'schema_version': '0.2.0'}):
            with self.subTest(change=change):
                self.assertFalse(self.validator.is_valid(self.response(**change)))

    def test_required_fields(self):
        for field in self.schema['required']:
            with self.subTest(field=field):
                response = self.response()
                del response[field]
                self.assertFalse(self.validator.is_valid(response))

    def test_text_fields(self):
        for field in ('primary_diagnosis', 'proposed_fix', 'limitations'):
            for value in ('x', 'x' * 1600):
                with self.subTest(field=field, length=len(value)):
                    self.validator.validate(self.response(**{field: value}))
            for value in ('', 'x' * 1601, 123):
                with self.subTest(field=field, value=value):
                    self.assertFalse(self.validator.is_valid(self.response(**{field: value})))
        self.assertFalse(self.validator.is_valid(self.response(limitations=None)))


if __name__ == '__main__':
    unittest.main()
