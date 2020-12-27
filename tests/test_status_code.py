import requests
import unittest
import json


class APITestCase_check_status_code(unittest.TestCase):

    # check status code
    def test_index(self):
        response = requests.get(
            'http://localhost:8080/')
        self.assertEqual(response.status_code, 200)

    def test2_index(self):
        response = requests.get(
            'http://localhost:8080/())*(*???//')
        self.assertEqual(response.status_code, 404)

    def test3_index(self):
        response = requests.post(
            'http://localhost:8080/')
        self.assertEqual(response.status_code, 405)

    def test1_home(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/home')
        self.assertEqual(response.status_code, 200)

    def test2_home(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/home/^&%^$%^')
        self.assertEqual(response.status_code, 404)

    def test3_home(self):
        response = requests.post(
            'http://localhost:8080/books-api/v1/resources/home')
        self.assertEqual(response.status_code, 405)

    def test_getAll(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getAll')
        self.assertEqual(response.status_code, 200)

    def test2_getAll(self):
        response = requests.post(
            'http://localhost:8080/books-api/v1/resources/getAll')
        self.assertEqual(response.status_code, 405)

    def test3_getAll(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getAll//')
        self.assertEqual(response.status_code, 404)

    def test1_getBook(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getbook?id=1')
        self.assertEqual(response.status_code, 200)

    def test2_getBook(self):
        response = requests.put(
            'http://localhost:8080/books-api/v1/resources/getbook?id=1')
        self.assertEqual(response.status_code, 405)

    def test3_getBook(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getb4454545)()(*)//')
        self.assertEqual(response.status_code, 404)

    def test4_getBook(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/getbook?id=-1')
        self.assertEqual(response.status_code, 400)

    # positive test with valid input
    def test1_add(self):
        data = {
            'title': 'War of worlds',
            'author': 'Jules vern',
            'publication': '1899-12-23'
        }
        response = requests.post(
            'http://localhost:8080/books-api/v1/resources/add',
            json=data)
        self.assertEqual(response.status_code, 200)

    # Negative test with invalid method
    def test2_add(self):
        data = {
            'title': 'War of worlds',
            'author': 'Jules vern',
            'publication': '1899-12-23'
        }
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/add',
            json=data)
        self.assertEqual(response.status_code, 405)

    # Negative test with invalid input
    def test3_add(self):
        data = {
            'title': 45,
            'author': 'Jules vern',
            'publication': '1855-12-10'
        }
        response = requests.post(
            'http://localhost:8080/books-api/v1/resources/add',
            data=data)
        self.assertEqual(response.status_code, 400)

    # Negative test with invalid url
    def test4_add(self):
        data = {
            'title': 'War of worlds',
            'author': 'Jules vern',
            'publication': "4545"
        }
        response = requests.post(
            'http://localhost:8080/books-api/v1/resources/add_(_)(_)//',
            json=data)
        self.assertEqual(response.status_code, 404)

    # positive test with valid inputs
    def test1_update(self):
        data = {
            'title': 'Submarines',
        }
        response = requests.put(
            'http://localhost:8080/books-api/v1/resources/update?id=2',
            json=data)
        self.assertEqual(response.status_code, 200)

    # negative test with invalid method
    def test2_update(self):
        data = {
            'title': 'Submarines',
        }
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/update?id=2',
            json=data)
        self.assertEqual(response.status_code, 405)

    # negative test with invalid input
    def test3_update(self):
        data = {
            'title': 'Submarines',
        }
        response = requests.put(
            'http://localhost:8080/books-api/v1/resources/update?id=foo-bar',
            json=data)
        self.assertEqual(response.status_code, 400)

    # negative test with invlaid url
    def test1_delete(self):

        response = requests.delete(
            'http://localhost:8080/books-api/v1/resources/delete/*/*(&*')
        self.assertEqual(response.status_code, 404)

    # negative test : invalid id
    def test2_delete(self):

        response = requests.delete(
            'http://localhost:8080/books-api/v1/resources/delete?id="##DS"')
        self.assertEqual(response.status_code, 400)
    # negative test : invalid method

    def test3_delete(self):

        response = requests.put(
            'http://localhost:8080/books-api/v1/resources/delete?id=7')
        self.assertEqual(response.status_code, 405)

    # negative test : missing id or invlid url
    def test4_delete(self):

        response = requests.delete(
            'http://localhost:8080/books-api/v1/resources/delete')
        self.assertEqual(response.status_code, 404)
