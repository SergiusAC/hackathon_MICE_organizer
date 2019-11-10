from miceapp import app


@app.cli.group()
def db():
    pass


@db.command()
def createall():
    from app import db
    from .models import AppUser
    db.create_all()
    admin = AppUser()
    admin.name = 'admin'
    admin.password = 'admin'
    admin.is_admin = True
    db.session.add(admin)
    db.session.commit()
