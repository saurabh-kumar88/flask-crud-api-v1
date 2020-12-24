import requests
import unittest
import json


class APITestCase_check_status_code(unittest.TestCase):

    # check status code
    def test_index(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/')
        self.assertEqual(response.status_code, 200)

    def test2_index(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/home///')
        self.assertEqual(response.status_code, 404)

    def test3_index(self):
        response = requests.post(
            'http://localhost:8080/books-api/v1/resources/')
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
            'http://localhost:8080/books-api/v1/resources/home/')
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
            'http://localhost:8080/books-api/v1/resources/update?id=8',
            json=data)
        self.assertEqual(response.status_code, 200)

    # negative test with invalid inputs
    # def test2_update(self):
    #     data = {
    #         'title': 'Submarines',
    #     }
    #     response = requests.put(
    #         'http://localhost:8080/books-api/v1/resources/update?id=8',
    #         json=data)
    #     self.assertEqual(response.status_code, 200)

    # def test3_update(self):
    #     data = {
    #         'title': 'Submarines',
    #     }
    #     response = requests.put(
    #         'http://localhost:8080/books-api/v1/resources/update?id=8',
    #         json=data)
    #     self.assertEqual(response.status_code, 200)

    # positive test with valid input
    def test1_delete(self):

        response = requests.delete(
            'http://localhost:8080/books-api/v1/resources/delete?id=21')
        self.assertEqual(response.status_code, 200)

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

        response = requests.put(
            'http://localhost:8080/books-api/v1/resources/delete')
        self.assertEqual(response.status_code, 404)


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


# check response/data


class APITestCase_check_data(unittest.TestCase):

    def test_index(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/')
        self.assertTrue(b'ok' in response.content)

    def test_home(self):
        response = requests.get(
            'http://localhost:8080/books-api/v1/resources/home')
        self.assertTrue(b'Welcome' in response.content)

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
            'http://localhost:8080/books-api/v1/resources/update?id=8',
            json=data)
        self.assertTrue(b'ok' in response.content)

    def test_delete(self):

        response = requests.put(
            'http://localhost:8080/books-api/v1/resources/update?id=8')
        self.assertTrue(b'ok' in response.content)
