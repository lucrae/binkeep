import os

BASE_DIR = os.path.abspath(os.path.dirname(__name__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '59af93ea593df66e9878818c08ac69e5fb5d77efe0943492' # development server key
    DEBUG = True
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.db')    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@localhost/linkbin'.format(os.environ.get('MYSQL_ROOT_PASSWORD'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False