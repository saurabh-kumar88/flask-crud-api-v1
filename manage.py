from flask_script import Manager
from app import app, db, dummyData, dropAll
from flask_migrate import Migrate, MigrateCommand


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def drop_all_tables():
    dropAll()


@manager.command
def init_dummy_data():
    dummyData()

@manager.command
def hello():
    print('hello world')



@manager.command
def runserver():
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == "__main__":
    manager.run()
