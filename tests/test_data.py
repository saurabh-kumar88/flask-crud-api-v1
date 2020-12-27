import requests
import unittest
import json

# check response/data


class APITestCase_check_data(unittest.TestCase):

    def test_getAll(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getAll')
        self.assertTrue(b'title' in response.content)

    def test_getBook(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getbook?id=1')
        self.assertTrue(b'author' in response.content)

    def test_add(self):
        data = {
            'title': 'War of worlds',
            'author': 'Jules vern',
            'publication': '1899-12-23'
        }
        response = requests.post(
            'http://localhost:8080/books-api/v1/resources/add',
            json=data)
        self.assertTrue(b'ok' in response.content)

    def test_update(self):
        data = {
            'title': 'Submarines',
        }
        response = requests.put(
            'http://localhost:8080/books-api/v1/resources/update?id=1',
            json=data)
        self.assertTrue(b'ok' in response.content)

    def test_delete(self):

        response = requests.delete(
            'http://localhost:8080/books-api/v1/resources/delete?id=19')
        self.assertTrue(b'ok' in response.content)
