"""

"""
# General imports
import json

# Partial imports
from unittest.mock import patch


# Imports from environment
from cornflow_client import get_pulp_jsonschema, get_empty_schema

# Imports from internal modules
from cornflow.app import create_app
from cornflow.tests.const import EXAMPLE_URL, INSTANCE_PATH
from cornflow.tests.custom_test_case import CustomTestCase


class TestExampleDataEndpoint(CustomTestCase):
    def setUp(self):
        super().setUp()

        def load_file(_file):
            with open(_file) as f:
                temp = json.load(f)
            return temp

        self.example = {"instance_1": load_file(INSTANCE_PATH)}
        self.url = EXAMPLE_URL
        self.schema_name = "solve_model_dag"

    def patch_af_client(self, Airflow_mock):
        af_client = Airflow_mock.return_value
        af_client.is_alive.return_value = True
        af_client.get_dag_info.return_value = {}
        af_client.get_one_variable.return_value = self.example
        af_client.get_all_schemas.return_value = [{"name": self.schema_name}]
        return af_client

    @patch("cornflow.endpoints.schemas.Airflow.from_config")
    def test_get_example(self, airflow_init):
        af_client = self.patch_af_client(airflow_init)
        example = self.get_one_row(
            self.url + "{}/".format(self.schema_name),
            {},
            expected_status=200,
            check_payload=False,
        )
        self.assertIn("examples", example)
        self.assertIn("name", example)
        self.assertEqual(example["examples"], self.example)
        af_client.is_alive.assert_called_once()
        af_client.get_dag_info.assert_called_once()
        af_client.get_schemas_for_dag_name.assert_called_once()
