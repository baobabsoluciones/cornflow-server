"""
Unit test for the permissions table
"""
# Import from libraries
import json

# Import from internal modules
from cornflow.endpoints import (
    PermissionsViewRoleEndpoint,
    PermissionsViewRoleDetailEndpoint,
)
from cornflow.shared.const import ROLES_MAP
from cornflow.tests.const import PERMISSION_URL
from cornflow.tests.custom_test_case import CustomTestCase


class TestPermissionsViewRoleEndpoint(CustomTestCase):
    def setUp(self):
        super().setUp()
        self.model = PermissionsViewRoleEndpoint
        self.roles_with_access = PermissionsViewRoleEndpoint.ROLES_WITH_ACCESS
        self.payload = {"role_id": 1, "permission_id": 1, "api_view_id": 1}

    def tearDown(self):
        super().tearDown()

    def test_get_permissions_view_role(self):
        for role in self.roles_with_access:
            self.token = self.create_user_with_role(role)

            response = self.client.get(
                PERMISSION_URL,
                follow_redirects=True,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + self.token,
                },
            )

            self.assertEqual(200, response.status_code)

    def test_get_no_permissions_view_role(self):
        for role in ROLES_MAP:
            if role not in self.roles_with_access:
                self.token = self.create_user_with_role(role)
                response = self.client.get(
                    PERMISSION_URL,
                    follow_redirects=True,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": "Bearer " + self.token,
                    },
                )

                self.assertEqual(403, response.status_code)

    def test_new_permission_authorized_user(self):
        api_view = 1
        for role in self.roles_with_access:
            self.token = self.create_user_with_role(role)
            payload = {"role_id": 1, "action_id": 3, "api_view_id": api_view}
            self.create_new_row(PERMISSION_URL, self.model, payload)
            api_view += 1

    def test_new_role_not_authorized(self):
        for role in ROLES_MAP:
            if role not in self.roles_with_access:
                self.token = self.create_user_with_role(role)
                self.create_new_row(
                    PERMISSION_URL,
                    self.model,
                    {},
                    expected_status=403,
                    check_payload=False,
                )


class TestPermissionViewRolesDetailEndpoint(CustomTestCase):
    def setUp(self):
        super().setUp()
        self.model = PermissionsViewRoleDetailEndpoint
        self.roles_with_access = PermissionsViewRoleDetailEndpoint.ROLES_WITH_ACCESS
        self.payload = {"role_id": 1, "action_id": 3, "api_view_id": 1}
        self.items_to_check = []

    def test_modify_permission_authorized_user(self):
        authorized_user = self.roles_with_access[0]
        self.token = self.create_user_with_role(authorized_user)

        self.id = self.client.post(
            PERMISSION_URL,
            follow_redirects=True,
            data=json.dumps(self.payload),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.token,
            },
        ).json["id"]
        for role in self.roles_with_access:
            if role != self.roles_with_access[0]:
                self.token = self.create_user_with_role(role)
            self.updated_payload = {"role_id": role, "action_id": 2}
            self.update_row(
                PERMISSION_URL + str(self.id) + "/",
                self.updated_payload,
                {"role_id": role, "action_id": 2, "api_view_id": 1},
            )

    def test_modify_permission_not_authorized(self):
        authorized_user = self.roles_with_access[0]
        self.token = self.create_user_with_role(authorized_user)
        self.id = self.client.post(
            PERMISSION_URL,
            follow_redirects=True,
            data=json.dumps(self.payload),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.token,
            },
        ).json["id"]
        for role in ROLES_MAP:
            if role not in self.roles_with_access:
                self.token = self.create_user_with_role(role)
                self.updated_payload = {"role_id": role, "action_id": 2}
                self.update_row(
                    PERMISSION_URL + str(id) + "/",
                    self.updated_payload,
                    {},
                    expected_status=403,
                    check_payload=False,
                )

    def test_delete_permission_authorized(self):
        for authorized_user in self.roles_with_access:
            self.token = self.create_user_with_role(authorized_user)
            id = self.client.post(
                PERMISSION_URL,
                follow_redirects=True,
                data=json.dumps(self.payload),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + self.token,
                },
            ).json["id"]

            response = self.client.delete(
                PERMISSION_URL + str(id) + "/",
                follow_redirects=True,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + self.token,
                },
            )

            self.assertEqual(501, response.status_code)

    def test_delete_permission_not_authorized(self):
        authorized_user = self.roles_with_access[0]
        self.token = self.create_user_with_role(authorized_user)
        id = self.client.post(
            PERMISSION_URL,
            follow_redirects=True,
            data=json.dumps(self.payload),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.token,
            },
        ).json["id"]

        for role in ROLES_MAP:
            if role not in self.roles_with_access:
                self.token = self.create_user_with_role(role)
                response = self.client.delete(
                    PERMISSION_URL + str(id) + "/",
                    follow_redirects=True,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": "Bearer " + self.token,
                    },
                )
                self.assertEqual(403, response.status_code)
