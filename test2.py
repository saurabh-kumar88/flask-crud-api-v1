import requests
import unittest


class APITestCase(unittest.TestCase):

    # check status code
    def test_status_code_index(self):
        response = requests.get(
            'http://localhost:8080/')
        assert response.status_code == 200

    def test_status_code_home(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/')
        assert response.status_code == 200

    def test_status_code_getAll(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getAll')
        assert response.status_code == 200

    def test_status_code_getBook(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getbook?id=1')
        assert response.status_code == 200

    # check content type

    def test_content_type_home(self):
        response = requests.post(
            'http://localhost:8080/books-api/v1/resources/')
        assert response.content_type == 'document'


# check status code

def test_get_status_code_index():
    response = requests.get(
        'http://localhost:8080/books-api/v1/resources/')
    assert response.status_code == 200


def test_get_status_code_home():
    response = requests.get(
        'http://localhost:8080/books-api/v1/resources/')
    assert response.status_code == 200


def test_get_status_code_getAll():
    response = requests.get(
        'http://localhost:8080/books-api/v1/resources/getAll')
    assert response.status_code == 200


def test_get_status_code_getBook():
    response = requests.get(
        'http://localhost:8080/books-api/v1/resources/getbook?id=1')
    assert response.status_code == 200
