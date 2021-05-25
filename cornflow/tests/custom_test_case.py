import json
from flask_testing import TestCase

from cornflow.app import create_app
from cornflow.models import UserModel
from cornflow.shared.utils import db
from cornflow.shared.authentication import Auth
from cornflow.tests.const import LOGIN_URL
from datetime import datetime, timedelta

try:
    date_from_str = datetime.fromisoformat
except:

    def date_from_str(_string):
        return datetime.strptime(_string, "%Y-%m-%d %H:%M:%S.%f")


class CustomTestCase(TestCase):
    def create_app(self):
        app = create_app("testing")
        return app

    @staticmethod
    def load_file(_file, fk=None, fk_id=None):
        with open(_file) as f:
            temp = json.load(f)
        if fk is not None and fk_id is not None:
            temp[fk] = fk_id
        return temp

    def setUp(self):
        db.create_all()
        data = {
            "name": "testname",
            "email": "test@test.com",
            "password": "testpassword",
        }
        user = UserModel(data=data)
        user.save()
        db.session.commit()
        data.pop("name")

        self.token = self.client.post(
            LOGIN_URL,
            data=json.dumps(data),
            follow_redirects=True,
            headers={"Content-Type": "application/json"},
        ).json["token"]

        self.user = Auth.return_user_from_token(self.token)
        self.url = None
        self.model = None
        self.copied_items = set()
        self.items_to_check = []

    @staticmethod
    def get_header_with_auth(token):
        return {"Content-Type": "application/json", "Authorization": "Bearer " + token}

    def create_super_admin(self):
        data = {
            "name": "airflow",
            "email": "airflow@baobabsoluciones.es",
            "password": "THISNEEDSTOBECHANGED",
        }

        user = UserModel(data=data)
        user.super_admin = True
        user.save()
        db.session.commit()
        data.pop("name")
        return self.client.post(
            LOGIN_URL,
            data=json.dumps(data),
            follow_redirects=True,
            headers={"Content-Type": "application/json"},
        ).json["token"]

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_new_row(
        self, url, model, payload, expected_status=201, check_payload=True
    ):

        response = self.client.post(
            url,
            data=json.dumps(payload),
            follow_redirects=True,
            headers=self.get_header_with_auth(self.token),
        )
        self.assertEqual(expected_status, response.status_code)
        if not check_payload:
            return response.json
        row = model.query.get(response.json["id"])
        self.assertEqual(row.id, response.json["id"])

        for key in self.get_keys_to_check(payload):
            self.assertEqual(getattr(row, key), payload[key])
        return row.id

    def get_rows(self, url, data):

        codes = [
            self.create_new_row(url=url, model=self.model, payload=d) for d in data
        ]
        rows = self.client.get(
            url, follow_redirects=True, headers=self.get_header_with_auth(self.token)
        )
        # rows now come in desc order of date, so we reverse them:
        rows_data = list(reversed(rows.json))
        self.assertEqual(len(rows.json), len(data))
        for i in range(len(data)):
            self.assertEqual(rows_data[i]["id"], codes[i])
            for key in self.get_keys_to_check(data[i]):
                self.assertEqual(rows_data[i][key], data[i][key])
        return rows

    def get_keys_to_check(self, payload):
        if len(self.items_to_check):
            return self.items_to_check & payload.keys()
        return payload.keys()

    def get_one_row(
        self, url, payload, expected_status=200, check_payload=True, token=None
    ):
        if token is None:
            token = self.token

        row = self.client.get(
            url, follow_redirects=True, headers=self.get_header_with_auth(token)
        )

        self.assertEqual(expected_status, row.status_code)
        if not check_payload:
            return row.json
        self.assertEqual(row.json["id"], payload["id"])
        for key in self.get_keys_to_check(payload):
            self.assertEqual(row.json[key], payload[key])
        return row.json

    def get_no_rows(self, url):
        rows = self.client.get(
            url, follow_redirects=True, headers=self.get_header_with_auth(self.token)
        )
        self.assertEqual(200, rows.status_code)
        return rows.json

    def update_row(
        self, url, change, payload_to_check, expected_status=200, check_payload=True
    ):
        response = self.client.put(
            url,
            data=json.dumps(change),
            follow_redirects=True,
            headers=self.get_header_with_auth(self.token),
        )
        self.assertEqual(expected_status, response.status_code)
        if not check_payload:
            return response.json
        row = self.client.get(
            url, follow_redirects=True, headers=self.get_header_with_auth(self.token)
        )

        self.assertEqual(200, row.status_code)
        self.assertEqual(row.json["id"], payload_to_check["id"])
        for key in self.get_keys_to_check(payload_to_check):
            self.assertEqual(row.json[key], payload_to_check[key])
        return row.json

    def delete_row(self, url):

        response = self.client.delete(
            url, follow_redirects=True, headers=self.get_header_with_auth(self.token)
        )
        self.assertEqual(200, response.status_code)

        response = self.client.get(
            url, follow_redirects=True, headers=self.get_header_with_auth(self.token)
        )

        self.assertEqual(404, response.status_code)
        return response

    def apply_filter(self, url, _filter, result):
        # we take out the potential query (e.g., ?param=1) arguments inside the url
        get_with_opts = lambda data: self.client.get(
            url.split("?")[0],
            follow_redirects=True,
            query_string=data,
            headers=self.get_header_with_auth(self.token),
        )
        response = get_with_opts(_filter)
        self.assertEqual(len(response.json), len(result))
        for k, v in enumerate(result):
            self.assertEqual(response.json[k], v)
        return

    def repr_method(self, idx, representation):
        row = self.model.query.get(idx)
        self.assertEqual(repr(row), representation)

    def str_method(self, idx, string: str):
        row = self.model.query.get(idx)
        self.assertEqual(str(row), string)


class BaseTestCases:
    class ListFilters(CustomTestCase):
        def setUp(self):
            self.payload = None
            super().setUp()

        def test_opt_filters_limit(self):
            # we create 4 instances
            data_many = [self.payload for _ in range(4)]
            allrows = self.get_rows(self.url, data_many)
            self.apply_filter(self.url, dict(limit=1), [allrows.json[0]])

        def test_opt_filters_offset(self):
            # we create 4 instances
            data_many = [self.payload for _ in range(4)]
            allrows = self.get_rows(self.url, data_many)
            self.apply_filter(self.url, dict(offset=1, limit=2), allrows.json[1:3])

        def test_opt_filters_schema(self):
            # we create 4 instances
            data_many = [self.payload for _ in range(4)]
            data_many[-1] = {**data_many[0], **dict(schema="timer")}
            allrows = self.get_rows(self.url, data_many)
            self.apply_filter(self.url, dict(schema="timer"), allrows.json[:1])

        def test_opt_filters_date_lte(self):
            # we create 4 instances
            data_many = [self.payload for _ in range(4)]
            allrows = self.get_rows(self.url, data_many)

            a = date_from_str(allrows.json[0]["created_at"])
            b = date_from_str(allrows.json[1]["created_at"])
            date_limit = b + (a - b) / 2
            # we ask for one before the last one => we get the second from the last
            self.apply_filter(
                self.url,
                dict(creation_date_lte=date_limit.isoformat(), limit=1),
                [allrows.json[1]],
            )

        def test_opt_filters_date_gte(self):
            # we create 4 instances
            data_many = [self.payload for _ in range(4)]
            allrows = self.get_rows(self.url, data_many)

            date_limit = date_from_str(allrows.json[2]["created_at"]) + timedelta(
                microseconds=1
            )
            # we ask for all after the third from the last => we get the last two
            self.apply_filter(
                self.url,
                dict(creation_date_gte=date_limit.isoformat()),
                allrows.json[:2],
            )
            return

        pass
