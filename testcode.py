import requests


def testcode():
    response = requests.get(
        'http://localhost:8080/books-api/v1/resources/')
    # print(response.content)
    if b'Message' in response.content:
        print(True)


if __name__ == "__main__":
    testcode()
