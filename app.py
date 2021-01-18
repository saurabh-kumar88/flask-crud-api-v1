import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, Response, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_script import Manager
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import asc, desc


# init Flask
app = Flask(__name__)

# Basic config with security for forms and session cookie

load_dotenv()

app.config['CSRF_ENABLED'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('HEROKU_POSTGRESQL_URI')


# database models
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    author = db.Column(db.String(25), unique=False, nullable=False)
    publication = db.Column(db.String(25), nullable=False)
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


def dropAll():
    db.drop_all()


# admin
admin = Admin(app, name='Flask crud api', template_mode='bootstrap4')
admin.add_view(ModelView(Book, db.session))


@app.route('/', methods=['GET'])
def index():
    if request.method != 'GET':
        return Response(status=405)
    elif request.method == 'GET':
        return render_template('index.html')
    else:
        return Response(status=404)


@app.route('/books-api/v1/resources/', methods=['GET'])
def home():
    if request.method != 'GET':
        return Response(405)

    elif request.method == 'GET':
        return render_template('index.html')
    else:
        return Response(status=404)


@app.route('/books-api/v1/resources/getAll', methods=['GET'])
def getAll():

    if request.method != 'GET':
        return Response(status=405)

    if request.method == 'GET':

        # --- optional query parameters ---

        # sqlalchemy query : sort by field name
        if 'sort' in request.args:
            sort = request.args['sort']
            if sort == 'title':
                books = Book.query.order_by(Book.title).all()
            elif sort == 'author':
                books = Book.query.order_by(Book.author).all()
            elif sort == 'latest':
                books = Book.query.order_by(asc(Book.created_At)).all()
            elif sort == 'oldest':
                books = Book.query.order_by(desc(Book.created_At)).all()
            else:
                return Response(status=404)
        if 'limit' in request.args:
            try:
                Limit = int(request.args['limit'])
            except ValueError as err:
                return Response(status=400)
            if Limit < 0:
                return Response(status=400)
            # sqlalchemy query : limit 'n' results
            try:
                books = Book.query.limit(Limit)
            except Exception as err:
                return Response(status=400)
        if 'skip' in request.args:
            try:
                skip = int(request.args['skip'])
            except ValueError as err:
                return Response(status=400)
            if skip < 0:
                return Response(status=400)
            # sqlalchemy query : skip 'n' initial results
            try:
                books = Book.query.offset(skip).all()
            except Exception as err:
                return Response(status=400)
        if 'page' in request.args:
            try:
                page = int(request.args['page'])
            except ValueError as err:
                return Response(status=400)
            if page < 0:
                return Response(status=400)
            # sqlalchemy query : pagination
            try:
                books = Book.query.paginate(
                    page, per_page=5, error_out=False).items
            except Exception as err:
                return Response(status=400)
        else:
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
    else:
        return Response(status=404)


@app.route('/books-api/v1/resources/getbook', methods=['GET'])
def getBook():

    result = []
    if request.method != 'GET':
        return Response(status=405)

    if "id" in request.args:
        try:
            id = int(request.args['id'])
        except ValueError as err:
            return Response(status=400)

        if id < 0:
            return Response(status=400)

        try:
            book = Book.query.get(id)
            result.append({"id": book.id})
            result.append({"title": book.title})
            result.append({"author": book.author})
            result.append({"publication": book.publication})
            return jsonify(result)
        except AttributeError as err:
            return Response(status=404)

    if 'title' in request.args and 'author' in request.args:
        try:
            Book.query.filter_by(
                title=request.args['title'], author=request.args['author']).all()
        except NoResultFound as err:
            return Response(status=404)
        else:
            books = Book.query.filter_by(
                title=request.args['title'], author=request.args['author'])

    if 'title' in request.args:
        try:
            Book.query.filter_by(title=request.args['title']).all()
        except NoResultFound as err:
            return Response(status=404)
        else:
            books = Book.query.filter_by(
                title=request.args['title'])

    if 'author' in request.args:
        try:
            Book.query.filter_by(author=request.args['author']).all()
        except NoResultFound as err:
            return Response(status=404)
        else:
            books = Book.query.filter_by(
                author=request.args['author'])

    for book in books:
        result.append({"id": book.id})
        result.append({"title": book.title})
        result.append({"author": book.author})
        result.append({"publcation": book.publication})
        result.append({"created_At": book.created_At})
        result.append({"updated_At": book.updated_At})
    if len(result) == 0:
        return Response(status=404)
    return jsonify(result)


@app.route('/books-api/v1/resources/add', methods=['POST'])
def addBook():

    if request.method != 'POST':
        return Response(status=405)

    elif request.method == 'POST':
        try:
            book = Book(title=request.json['title'], author=request.json['author'],
                        publication=request.json['publication'])
            db.session.add(book)
            db.session.commit()
            return jsonify("ok")
        except Exception as err:
            return Response(status=400)


@app.route('/books-api/v1/resources/delete', methods=['DELETE'])
def deleteBook():

    if request.method != 'DELETE':
        return Response(status=405)

    if request.method == 'DELETE':
        if 'id' in request.args:
            try:
                id = int(request.args['id'])
            except ValueError as err:
                return Response(status=400)

            try:
                book = Book.query.filter_by(id=id).one()
                db.session.delete(book)
                db.session.commit()
                return jsonify('ok')
            except NoResultFound as err:
                return Response(status=404)
        else:
            return Response(status=404)


@app.route('/books-api/v1/resources/update', methods=['PUT'])
def updateBook():
    result = []
    if request.method != 'PUT':
        return Response(status=405)

    if request.method == 'PUT':
        if 'id' in request.args:
            try:
                id = int(request.args['id'])
            except ValueError as err:
                return Response(status=400)

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
                return Response(status=400)
        else:
            return Response(status=404)
