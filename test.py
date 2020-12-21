try:
    import unittest
    from run import app
except ImportError as err:
    print('Some modules not imported : {}'.format(err))


class FlaskTestCase(unittest.TestCase):

    # check response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type, 'application/json')

    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertTrue(b'Message' in response.data)

    # def test_getAll_content(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/books-api/v1/resources/getAll')
    #     self.assertEqual(response, 'application/json')


if __name__ == "__main__":
    unittest.main()
