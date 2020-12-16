import mysql.connector as db

class MYSQLDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.mydb = db.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def create_db(self, db_name):
        cursor = self.mydb.cursor()
        cursor.execute("CREATE DATABASE {} IF NOT EXISTS".format(db_name))

    def show_db(self):
        cursor = self.mydb.cursor()
        cursor.execute("SHOW DATABASES")
        databases = []
        for db in cursor:
            databases.append(db)
        return databases

    def create_table(self, table_name, table_schema):
        cursor = db.cursor()
        try:
            cursor.execute("CREATE TABLE {} IF NOT EXISTS ({})".format(table_name, table_schema ))
            print("{} created successfully!".format(table_name))
        except Exception as e:
            print(e)
            return

    def insert_into_table(self, table_name, table_shcema, values):
        pass

    def delete_from_table(self):
        pass

    def update_from_table(self):
        pass


if __name__ == '__main__':
    obj = MYSQLDB(
        host="localhost",
        user="root",
        password="saw99",
        database="testdb"
    )


    books_schema = """
    (id INT AUTO_INCREMENT PRIMARY KEY),
    (title VARCHAR(25)),
    (author VARCHAR(25)),
    (published VARCHAR(25)),
    """

    obj.create_table(table_name="books", table_schema=books_schema)



