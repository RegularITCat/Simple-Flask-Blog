from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from os import urandom
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = urandom(24)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
