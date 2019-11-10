from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login = LoginManager()
login.login_view = 'login'


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    login.init_app(app)

    return app
