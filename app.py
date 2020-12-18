import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# init Flask
app = Flask(__name__)

# Basic config with security for forms and session cookie

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:saw99@localhost/testdb'
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'thisismyscretkey'


# database models
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    author = db.Column(db.String(25), unique=False, nullable=False)
    publication = db.Column(db.String(20), nullable=False)
    created_At = db.Column(db.DateTime, server_default=db.func.now())
    updated_At = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return self.title


def dummyData():
    books = []
    books.append({"title": "Ready player two",
                  "author": "Ernest Cline", "publication": "2020-10-04"})
    books.append({"title": "Stuff You Should Know",
                  "author": "Book by Josh Clark", "publication": "2020-11-24"})
    books.append({"title": "The Greatest Secret",
                  "author": "Book by Rhonda Byrne", "publication": "2020-11-24"})
    books.append({"title": "A Promised Land",
                  "author": "Book by Barack Obama", "publication": "2020-11-17"})
    books.append({"title": "Home Body",
                  "author": "Book by Rupi Kaur", "publication": "2020-11-17"})
    books.append({"title": "The Ickabog",
                  "author": "Book by J. K. Rowling", "publication": "2020-11-10"})

    for data in books:
        dummy_data = Book(
            title=data['title'], author=data['author'], publication=data['publication'])
        try:
            db.session.add(dummy_data)
            db.session.commit()
        except Exception as e:
            print(e)


# db.create_all()
# db.drop_all()
# dummyData()

# admin
admin = Admin(app, name='Flask crud api', template_mode='bootstrap4')
admin.add_view(ModelView(Book, db.session))


@app.route('/', methods=['GET'])
def index():
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


@app.route('/books-api/v1/resources/', methods=['GET'])
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
    books = Book.query.all()
    result = []
    for book in books:
        result.append({"title": book.title})
        result.append({"author": book.author})
        result.append({"publcation": book.publication})
    return jsonify(result)


# @app.route('/books-api/v1/resources/getbook', methods=['GET'])
# def getBook():
#     # Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.

#     if "id" in request.args:
#         id = int(request.args['id'])
#     else:
#         return "ERROR : No id provided for book record, please specify a book id."

#     result = []
#     # check if id exists
#     for book in books:
#         if book['id'] == id:
#             result.append(book)
#     if len(result) == 0:
#         return "ERROR : This book id does not exist!"
#     else:
#         return jsonify(result)


@app.route('/books-api/v1/resources/add', methods=['POST'])
def addBook():

    if request.method == 'POST':
        book = Book(title=request.json['title'], author=request.json['author'],
                    publication=request.json['publication'])
        db.session.add(book)
        db.session.commit()
    else:
        return "ERROR : Invalid data, please specify id"

    return "book added"


# @app.route('/books-api/v1/resources/delete', methods=['DELETE'])
# def deleteBook():
#     if request.method == 'DELETE':
#         id = int(request.json['id'])
#         for book in books:
#             if id == book['id']:
#                 books.remove(book)
#                 break
#     else:
#         return "ERROR : Invalid id, please specify correct id"
#     return "book has been deleted"


# @app.route('/books-api/v1/resources/update', methods=['PUT'])
# def updateBook():
#     isUpdated = False
#     if request.method == 'PUT':
#         # check for valid id
#         id = int(request.args['id'])

#         for book in books:
#             if id == book['id']:
#                 book['author'] = request.json['author']
#                 isUpdated = True
#                 break

#                 # if request.json['title']:
#                 #     book['title'] = request.json['title']
#                 # if request.json['published']:
#                 #     book['published'] = request.json['published']
#                 # if request.json['author']:
#                 #     book['author'] = request.json['author']

#     return "Updated" if isUpdated else "Invalid ID"


# Run the development server
if __name__ == "__main__":
    # manager.run()
    app.run(host='0.0.0.0', port=8080, debug=True)
