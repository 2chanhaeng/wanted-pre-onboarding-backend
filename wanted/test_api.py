from django.test import TestCase
import requests
import json

test_len = 3


class CreateApiTestCase(TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/wanted/"
        self.headers = {"Content-Type": "application/json"}

    def test_create_company(self) -> None:
        # 회사 생성
        data = {"name": "test_company"}
        response = requests.post(
            self.url + "company/", data=json.dumps(data), headers=self.headers
        )
        self.assertEqual(response.status_code, 201)

    def test_create_user(self) -> None:
        # 유저 생성
        data = {"name": "test_user"}
        response = requests.post(
            self.url + "user/", data=json.dumps(data), headers=self.headers
        )
        self.assertEqual(response.status_code, 201)

    def test_create_notice(self) -> None:
        # 채용공고 생성
        data = {"name": "test_notice", "company": 1}
        response = requests.post(
            self.url + "notice/", data=json.dumps(data), headers=self.headers
        )
        self.assertEqual(response.status_code, 201)

    def test_create_application(self) -> None:
        # 지원내역 생성
        data = {"notice": 1, "user": 1}
        response = requests.post(
            self.url + "application/", data=json.dumps(data), headers=self.headers
        )
        self.assertEqual(response.status_code, 201)


class ReadApiTestCase(TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/wanted/"
        self.headers = {"Content-Type": "application/json"}

    def test_read_company(self) -> None:
        # 회사 조회
        response = requests.get(self.url + "company/1/")
        self.assertEqual(response.json(), {"name": "test_company"})

    def test_read_user(self) -> None:
        # 유저 조회
        response = requests.get(self.url + "user/1/")
        self.assertEqual(response.json(), {"name": "test_user"})

    def test_read_notice(self) -> None:
        # 채용공고 조회
        response = requests.get(self.url + "notice/1/")
        self.assertEqual(response.json(), {"name": "test_notice", "company": 1})

    def test_read_application(self) -> None:
        # 지원내역 조회
        response = requests.get(self.url + "application/1/")
        self.assertEqual(response.json(), {"notice": 1, "user": 1})


class UpdateApiTestCase(TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/wanted/"
        self.headers = {"Content-Type": "application/json"}

    def test_update_company(self) -> None:
        # 회사 수정
        data = {"name": "updated_company"}
        response = requests.put(
            self.url + "company/1/", data=json.dumps(data), headers=self.headers
        )
        self.assertEqual(response.status_code, 200)

    def test_update_user(self) -> None:
        # 유저 수정
        data = {"name": "updated_user"}
        response = requests.put(
            self.url + "user/1/", data=json.dumps(data), headers=self.headers
        )
        self.assertEqual(response.status_code, 200)

    def test_update_notice(self) -> None:
        # 채용공고 수정
        data = {"name": "updated_notice"}
        response = requests.put(
            self.url + "notice/1/", data=json.dumps(data), headers=self.headers
        )
        self.assertEqual(response.status_code, 200)


class DeleteApiTestCase(TestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/wanted/"
        self.headers = {"Content-Type": "application/json"}

    def test_delete_company(self) -> None:
        # 회사 삭제
        response = requests.delete(self.url + "company/1/")
        self.assertEqual(response.status_code, 204)

    def test_delete_user(self) -> None:
        # 유저 삭제
        response = requests.delete(self.url + "user/1/")
        self.assertEqual(response.status_code, 204)

    def test_delete_notice(self) -> None:
        # 채용공고 삭제
        response = requests.delete(self.url + "notice/1/")
        self.assertEqual(response.status_code, 204)

    def test_delete_application(self) -> None:
        # 지원내역 삭제
        response = requests.delete(self.url + "application/1/")
        self.assertEqual(response.status_code, 204)
