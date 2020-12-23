import os
from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_script import Manager
from sqlalchemy.orm.exc import NoResultFound

# init Flask
app = Flask(__name__)

# Basic config with security for forms and session cookie

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


# database models
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    author = db.Column(db.String(25), unique=False, nullable=False)
    publication = db.Column(db.String(20), nullable=False)
    created_At = db.Column(db.DateTime, server_default=db.func.now())
    updated_At = db.Column(
        db.DateTime, onupdate=db.func.now())

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


# drop all tables
if 0:
    db.drop_all()

# create table and insert dummy data
if 0:
    db.create_all()
    dummyData()

# admin
admin = Admin(app, name='Flask crud api', template_mode='bootstrap4')
admin.add_view(ModelView(Book, db.session))


@app.route('/books-api/v1/resources/', methods=['GET'])
def index():
    return jsonify({'Message': 'ok'})


@app.route('/books-api/v1/resources/home', methods=['GET'])
def home():
    # print("\n ****************** ")
    # print(request.code)
    if request.method == 'GET':
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
    else:
        return "error"


# @app.after_request
# def log_status_code(response):
#     print("\n ****************** ")
#     print(response.status)


@app.route('/books-api/v1/resources/getAll', methods=['GET'])
def getAll():
    books = Book.query.all()
    result = []
    for book in books:
        result.append({"id": book.id})
        result.append({"title": book.title})
        result.append({"author": book.author})
        result.append({"publcation": book.publication})
        result.append({"created_At": book.created_At})
        result.append({"updated_At": book.updated_At})
    return jsonify(result)


@app.route('/books-api/v1/resources/getbook', methods=['GET'])
def getBook():

    if "id" in request.args:
        id = int(request.args['id'])
    else:
        return "ERROR : No id provided for book record, please specify a book id."

    result = []

    try:
        book = Book.query.get(id)
        result.append({"id": book.id})
        result.append({"title": book.title})
        result.append({"author": book.author})
        result.append({"publication": book.publication})
        return jsonify(result)
    except AttributeError as err:
        return "Error : Invalid book id"


@app.route('/books-api/v1/resources/add', methods=['POST'])
def addBook():

    if request.method == 'POST':
        book = Book(title=request.json['title'], author=request.json['author'],
                    publication=request.json['publication'])
        db.session.add(book)
        db.session.commit()
    else:
        return "ERROR : Invalid data, please specify id"

    return jsonify("ok")


@app.route('/books-api/v1/resources/delete', methods=['DELETE'])
def deleteBook():

    if 'id' in request.args.keys():
        id = int(request.args['id'])
    else:
        return "Error : Book id is missing!"
    if request.method == 'DELETE':
        id = int(request.args['id'])
        try:
            book = Book.query.filter_by(id=id).one()
            db.session.delete(book)
            db.session.commit()
            return jsonify('ok')
        except NoResultFound as err:
            return "Error : Invalid book id"


@app.route('/books-api/v1/resources/update', methods=['PUT'])
def updateBook():
    result = []
    if 'id' in request.args.keys():
        id = int(request.args['id'])
    else:
        return "Error : Book id is missing!"

    if request.method == 'PUT':
        try:
            book = Book.query.get(id)
            if 'title' in request.json.keys():
                book.title = request.json['title']
            if 'author' in request.json.keys():
                book.author = request.json['author']
            if 'publication' in request.json.keys():
                book.publication = request.json['publication']

            db.session.add(book)
            db.session.commit()

            result.append({'id': book.id})
            result.append({'title': book.title})
            result.append({'author': book.author})
            result.append({'publication': book.publication})
            result.append({'created_At': book.created_At})
            result.append({'updated_At': book.updated_At})
            return jsonify("ok")
        except AttributeError as err:
            return "Error : Invalid book id"


# Run the development server
if __name__ == "__main__":
    # manager.run()
    app.run(host='0.0.0.0', port=8080, debug=True)
