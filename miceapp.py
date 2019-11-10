from app import create_app, login
from config import Config


app = create_app(Config)


@login.user_loader
def user_loader(id):
    from app.models import AppUser
    return AppUser.query.get(id)


from app.routes import *
from app.models import *
from app.cli import *
