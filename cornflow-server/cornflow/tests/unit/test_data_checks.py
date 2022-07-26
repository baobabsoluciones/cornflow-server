"""
Unit test for the data check endpoint
"""

# Import from libraries
import json

# Import from internal modules
from cornflow.models import ExecutionModel, InstanceModel
from cornflow.tests.const import (
    INSTANCE_PATH,
    EXECUTION_PATH,
    EXECUTION_URL_NORUN,
    DATA_CHECK_EXECUTION_URL,
    DATA_CHECK_INSTANCE_URL,
    INSTANCE_URL,
)
from cornflow.tests.custom_test_case import CustomTestCase


class TestDataChecksExecutionEndpoint(CustomTestCase):
    def setUp(self):
        super().setUp()

        with open(INSTANCE_PATH) as f:
            payload = json.load(f)
        fk_id = self.create_new_row(INSTANCE_URL, InstanceModel, payload)
        self.model = ExecutionModel

        def load_file_fk(_file):
            with open(_file) as f:
                temp = json.load(f)
            temp["instance_id"] = fk_id
            return temp

        self.payload = load_file_fk(EXECUTION_PATH)

    def test_check_execution(self):
        exec_to_check_id = self.create_new_row(
            EXECUTION_URL_NORUN,
            self.model,
            payload=self.payload
        )
        url = DATA_CHECK_EXECUTION_URL + exec_to_check_id + "/?run=0"
        response = self.client.post(
            url,
            follow_redirects=True,
            headers=self.get_header_with_auth(self.token),
        )

        self.assertEqual(201, response.status_code)
        response = response.json

        row = self.model.query.get(response["id"])
        self.assertEqual(row.id, response["id"])
        self.assertEqual(row.id, exec_to_check_id)


class TestDataChecksInstanceEndpoint(CustomTestCase):
    def setUp(self):
        super().setUp()

        with open(INSTANCE_PATH) as f:
            payload = json.load(f)
        fk_id = self.create_new_row(INSTANCE_URL, InstanceModel, payload)
        self.instance_id = fk_id
        self.model = ExecutionModel

    def test_new_data_check_execution(self):

        url = DATA_CHECK_INSTANCE_URL + self.instance_id + "/?run=0"
        response = self.client.post(
            url,
            follow_redirects=True,
            headers=self.get_header_with_auth(self.token),
        )

        self.assertEqual(201, response.status_code)
        response = response.json

        row = self.model.query.get(response["id"])
        self.assertEqual(row.id, response["id"])

        self.assertEqual(row.instance_id, self.instance_id)
        self.assertTrue(row.config.get("checks_only"))
