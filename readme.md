<h1><b>Live at http://flask-crud-api-v1.herokuapp.com/</b></h1>

<h4>Step 1: copy this repository github link</h4>
<img src="https://github.com/saurabh-kumar88/flask-crud-api-v1/blob/main/docs/clone%20repo.png">
<h4>Step 1.1: Create your project folder/dir</h4>
<h4>Step 1.2: cd to project folder</h4>
<h4>Step 1.3: Clone repository -> run git clone "link"</h4>
<h4>Step 2: cd to colned project dir</h4>
<h4>Step 2.1: create virtual environment to install python dependecies by</h4>
<h4>run python -m virtualenv venv</h4>
<h4>Step 2.2: cd venv/Scripts then run ./activate or activate (this will activate virtual environment)</h4>
<h4>Step 2.3: TO disable virtual environment just run deactivate</h4>
<h4>Step 2.4: cd to project folder, now install all python dependencies listed in requiremenst.txt file</h4>
<h4>run pip install -r requirements.txt</h4>
<h4>Step 4: Set environment variables</h4>
<h4>Step 4.1: Create a file into the root dir and name it .env (this will holds our environment variables)</h4>
<h4>Step 4.2: Define these environment variables in .env file</h4>
<h4>SQLALCHEMY_DATABASE_URI="mysql://username:password@server/db"</h4>
<h4>or if you are using postgreSQL</h4>
<h4>SQLALCHEMY_DATABASE_URI="postgres+psycopg2://username:password@server/db"</h4>
<h4>SECRET_KEY="thisismyscretkey"</h4>
<h4>DEBUG=True</h4>
<h4>step 5: Start dev server by</h4>
<h4>run python manage.py runserver</h4>
<h4>if every things okay then your console should look like this</h4><br>
<img src="https://github.com/saurabh-kumar88/flask-crud-api-v1/blob/main/docs/console%20running%20dev%20server.png">
<br>
<h1>API endpoints description</h1>

1. GET http://localhost:3000/books-api/v1/resources/

   <br>
   description : Index page, descripton of all endpoints
    <br>
   response : Application/json

2. GET http://localhost:3000/books-api/v1/resources/getAll
   <br>
   description : Get All records
   <br>
   response : Application/json

3. GET http://localhost:3000/books-api/v1/resources/getAll?page=n
   <br>
   description : Pagination (n = page number)
   <br>
   response : "Application/json"

4. GET http://localhost:3000/books-api/v1/resources/getAll?sort=oldest
   <br>
   description : Sorting all records, oldest first
   <br>
   sorting order can by : oldest, latest, title, author
   <br>
   response : Application/json

5. GET http://localhost:3000/books-api/v1/resources/getAll?limit=n
   <br>
   description : limit records by n numbers
   <br>
   response : Application/json

6. GET http://localhost:3000/books-api/v1/resources/getAll?skip=n
   <br>
   description : Skip n initial records

   <br>
   response : Application/json

7. GET http://localhost:3000/books-api/v1/resources/getbook?id=n
   <br>
   description : Get a single record by its id
   <br>
   response : Appliation/json

8. GET http://localhost:3000/books-api/v1/resources/getbook?author="author name"
   <br>
   description : Search books by author name

   <br>
   response : Application/json

9. GET http://localhost:3000/books-api/v1/resources/getbook?title="book title"
   <br>
   description : Search book by its title

   <br>
   response : Application/json

10. GET http://localhost:3000/books-api/v1/resources/getbook?title="book title"&author="author name"
    <br>
    description : Combined search providing title and author name
    <br>
    response : Application/json

11. POST http://localhost:3000/books-api/v1/resources/add
    <br>
    description : Add new book record
    <br>
    body = {
    "title" : "book title",
    "author" : "author name",
    "publication" : "publication date"
    }
    <br>
    response : "ok"

12. PUT http://localhost:3000/books-api/v1/resources/update?id=n
    <br>
    description : Update a book record by its id
    <br>
    body = {
    "title" : "book title",
    "author" : "author name",
    "publication" : "publication date"
    }
    <br>
    response : "ok"

13. DELETE http://localhost:3000/books-api/v1/resources/delete?id=n
    <br>
    description : Delete a book record by its id
    <br>
    response : "ok"
