from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from os import urandom
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security, current_user
from flask import redirect, url_for, request

app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = urandom(24)
db = SQLAlchemy(app)

# Flask migrate
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Flask admin
class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))

class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)

class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['tags', 'title', 'body']

class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']

class AdminView(AdminMixin, ModelView):
    pass

class HomeAdminView(AdminMixin, AdminIndexView):
    pass

from models import *
admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))

# Flask security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
