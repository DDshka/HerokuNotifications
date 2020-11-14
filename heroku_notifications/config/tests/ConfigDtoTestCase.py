from django.test import TransactionTestCase

from pydantic import ValidationError

from heroku_notifications.config.dtos import ConfigDto
from heroku_notifications.config.tests import config_jsons


class ConfigDtoTestCase(TransactionTestCase):
    def test_valid_cases(self):
        for case_name, case_data in config_jsons.valid_cases.items():
            with self.subTest(msg=case_name):
                dto = ConfigDto(**case_data)
                self.assertNotEqual(dto, None)

    def test_invalid_cases(self):
        for case_name, case_data in config_jsons.invalid_cases.items():
            with self.subTest(msg=case_name):
                with self.assertRaises(ValidationError):
                    ConfigDto(**case_data)
