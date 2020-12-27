import requests


def testcode():
    response = requests.get(
        'https://www.geeksforgeeks.org/')
    print(response.headers)
    # print(response.content)
    # if b'Message' in response.content:
    #     print(True)


def add():
    data = {
        'title': 'I robot',
        'author': 'Asimove ivo',
        'publication': '1975-12-23'
    }
    response = requests.post(
        'http://localhost:8080/books-api/v1/resources/add', json=data
    )

    print(response.status_code)


if __name__ == "__main__":
    # testcode()
    # add()
    x = "45"
    try:
        int(x, base=10)
    except TypeError as err:
        print(err)


# "sudo rsync -rv C:\Projects\PYTHON\API\FLASK-CRUD-API/ ubuntu@192.168.1.1:/home/ubuntu/flask_api"
