import requests
import unittest
import json


class APITestCase_check_content_type(unittest.TestCase):

    # check content type

    def test_index(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/')
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_home(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/home')
        self.assertEqual(
            response.headers['content-type'], 'text/html; charset=utf-8')

    def test_getAll(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getAll')
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_getBook(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getbook?id=2')
        self.assertEqual(response.headers['content-type'], 'application/json')
