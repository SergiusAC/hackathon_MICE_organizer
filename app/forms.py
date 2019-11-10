from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import *


class AddEventForm(FlaskForm):
    name = StringField('Название', validators=[Optional()])
    date = DateField('Дата проведения', validators=[Optional()])
    desc = StringField('Описание', validators=[Optional()])
    category = StringField('Категория', validators=[Optional()])
    price = FloatField('Цена за билет', validators=[Optional()])
    lat = FloatField('Lat', validators=[Optional()])
    lng = FloatField('Lng', validators=[Optional()])
    count_places = IntegerField('Количество мест', validators=[Optional()])
    quests_was = IntegerField('Количество гостей', validators=[Optional()])


class LoginForm(FlaskForm):
    name = StringField('Имя организации', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    name = StringField('Имя организации', validators=[DataRequired()])
    subject = StringField('Деятельность', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
