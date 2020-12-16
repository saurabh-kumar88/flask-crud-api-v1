import flask
from flask import jsonify, request
from flask_admin import Admin

app = flask.Flask(__name__)
admin = Admin(app, "My Admin")
app.config["DEBUG"] = True

# DATA
books = [{"id": 0,
          "title": "The way back",
          "published": "1992",
          "author": "HG Wells"},
         {"id": 1,
          "title": "The time machine",
          "published": "1879",
          "author": "Jules vern"},
         {"id": 2,
          "title": "Space race",
          "published": "1975",
          "author": "Warner von brown"}]


@app.route('/', methods=['GET'])
def home():
    return '''
    <h1>Welcome to flask-crud api demo</h1>
    <ol>
        <li>crud-api/getAll : get all books record</li>
        <li>crud-api/getbook/id : get a book record by its id</li>
        <li>crud-api/add : add new book</li>
        <li>crud-api/delete/id : remove a book record</li>
        <li>crud-api/put/id : update a book record</li>
    </ol>
    '''


@app.route('/books-api/v1/resources/getAll', methods=['GET'])
def getAll():
    return jsonify(books)


@app.route('/books-api/v1/resources/getbook', methods=['GET'])
def getBook():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.

    if "id" in request.args:
        id = int(request.args['id'])
    else:
        return "ERROR : No id provided for book record, please specify a book id."

    result = []
    # check if id exists
    for book in books:
        if book['id'] == id:
            result.append(book)
    if len(result) == 0:
        return "ERROR : This book id does not exist!"
    else:
        return jsonify(result)


@app.route('/books-api/v1/resources/add', methods=['POST'])
def addBook():
    result = []
    if request.method == 'POST':
        result.append(int(request.json['id']))
        result.append(request.json['title'])
        result.append(request.json['published'])
        result.append(request.json['author'])
    else:
        return "ERROR : Invalid data, please specify id"

    return jsonify(result)


@app.route('/books-api/v1/resources/delete', methods=['DELETE'])
def deleteBook():
    if request.method == 'DELETE':
        id = int(request.json['id'])
        for book in books:
            if id == book['id']:
                books.remove(book)
                break
    else:
        return "ERROR : Invalid id, please specify correct id"
    return "book has been deleted"


@app.route('/books-api/v1/resources/update', methods=['PUT'])
def updateBook():
    isUpdated = False
    if request.method == 'PUT':
        # check for valid id
        id = int(request.args['id'])

        for book in books:
            if id == book['id']:
                book['author'] = request.json['author']
                isUpdated = True
                break

                # if request.json['title']:
                #     book['title'] = request.json['title']
                # if request.json['published']:
                #     book['published'] = request.json['published']
                # if request.json['author']:
                #     book['author'] = request.json['author']

    return "Updated" if isUpdated else "Invalid ID"


app.run()
