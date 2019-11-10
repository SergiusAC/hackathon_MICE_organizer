import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{path}'.format(path=os.path.join(basedir, 'database.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
