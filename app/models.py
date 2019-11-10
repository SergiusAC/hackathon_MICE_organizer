from app import db
from flask_login import UserMixin


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date = db.Column(db.Date)
    desc = db.Column(db.String)
    category = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Float)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    count_places = db.Column(db.Integer)
    count_quests_was = db.Column(db.Integer)

    organizer_id = db.Column(db.Integer, db.ForeignKey('app_user.id'))


class AppUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    subject = db.Column(db.String)
    city = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    events = db.relationship('Event', backref='user', lazy=True)


# class Organizer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     website = db.Column(db.String)


# class Tour(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
#     description = db.Column(db.String(255))
#
#     places = db.relationship('Place', backref='tour', lazy=True)
#
#
# class Place(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
#     description = db.Column(db.String(255))
#     price = db.Column(db.Float)
#     lat = db.Column(db.Float)
#     lng = db.Column(db.Float)
#
#     tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'))
#     excursion_id = db.Column(db.Integer, db.ForeignKey('excursion.id'))
#
#
# class Excursion(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
#     description = db.Column(db.String(255))
#     price = db.Column(db.Float)
#
#     places = db.relationship('Place', backref='excursion', lazy=True)
