import requests
import unittest
import json


class APITestCase_StatusCode(unittest.TestCase):

    # check status code
    def test_status_code_index(self):
        response = requests.get(
            'http://localhost:8080/')
        self.assertEqual(response.status_code, 200)

    def test_status_code_home(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/')
        self.assertEqual(response.status_code, 200)

    def test_status_code_getAll(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getAll')
        self.assertEqual(response.status_code, 200)

    def test_status_code_getBook(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getbook?id=1')
        self.assertEqual(response.status_code, 200)

    def test_status_code_add(self):
        data = {
            'title': 'War of worlds',
            'author': 'Jules vern',
            'publication': '1899-12-23'
        }
        response = requests.post(
            'http://localhost:8080/books-api/v1/resources/add',
            json=data)
        self.assertEqual(response.status_code, 200)

    def test_status_code_update(self):
        data = {
            'title': 'Submarines',
        }
        response = requests.put(
            'http://localhost:8080/books-api/v1/resources/update?id=8',
            json=data)
        self.assertEqual(response.status_code, 200)

    def test_status_code_delete(self):

        response = requests.delete(
            'http://localhost:8080/books-api/v1/resources/delete?id=8')
        self.assertEqual(response.status_code, 200)


class APITestCase_Content_Type(unittest.TestCase):

    # check content type

    def test_content_type_index(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/')
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_content_type_getAll(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getAll')
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_content_type_getBook(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getbook?id=2')
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_content_type_home(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/home')
        self.assertEqual(
            response.headers['content-type'], 'text/html; charset=utf-8')


class APITestCase_Check_Data(unittest.TestCase):

    def test_data_index(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/')
        self.assertTrue(b'Message' in response.content)

    def test_data_home(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/home')
        self.assertTrue(b'Welcome' in response.content)

    def test_data_getAll(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getAll')
        self.assertTrue(b'title' in response.content)

    def test_data_getBook(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getbook?id=1')
        self.assertTrue(b'author' in response.content)

    def test_data_add(self):
        data = {
            'title': 'War of worlds',
            'author': 'Jules vern',
            'publication': '1899-12-23'
        }
        response = requests.post(
            'http://localhost:8080/books-api/v1/resources/add',
            json=data)
        self.assertTrue(b'book added' in response.content)

    def test_data_update(self):
        data = {
            'title': 'Submarines',
        }
        response = requests.put(
            'http://localhost:8080/books-api/v1/resources/update?id=8',
            json=data)
        self.assertTrue(b'id' in response.content)

    def test_data_delete(self):

        response = requests.put(
            'http://localhost:8080/books-api/v1/resources/update?id=8')
        self.assertTrue(b'id' in response.content)
