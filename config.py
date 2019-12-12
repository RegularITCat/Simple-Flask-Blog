class Configuration(object):
    # Flask configuration
    DEBUG = True

    # SQLAlchemy configuration
    # pls don't hack me(((99(((
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost/flask_test1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
