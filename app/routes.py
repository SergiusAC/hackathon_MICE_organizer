from flask import render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user

from miceapp import app
from .forms import AddEventForm, LoginForm, RegistrationForm
from .models import Event, AppUser
from . import db


@app.route('/', methods=['GET'])
def index():
    return render_template('app_base.html')


@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    form = AddEventForm()
    if form.validate_on_submit():
        event = Event()
        event.name = form.name.data
        event.desc = form.desc.data
        event.category = form.category.data
        event.date = form.date.data
        event.price = form.price.data
        event.count_places = form.count_places.data
        event.lat = form.lat.data
        event.lng = form.lng.data
        event.organizer_id = current_user.id
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('add_event'))
    return render_template('add_event.html', form=form)


@app.route('/show_event/<int:id>', methods=['GET', 'POST'])
def show_event(id):
    event = Event.query.get(id)
    return render_template('show_event.html', event=event)


@app.route('/events_list', methods=['GET'])
def events_list():
    events = Event.query.filter_by(organizer_id=current_user.id).all()
    return render_template('events_list.html', events=events)


@app.route('/admin/', methods=['GET'])
def admin_index():
    return render_template('admin/index.html')


@app.route('/admin/orgs', methods=['GET'])
def admin_orgs():
    orgs = AppUser.query.filter_by(is_admin=False).all()
    return render_template('admin/orgs_list.html', orgs=orgs)


@app.route('/admin/events', methods=['GET'])
def admin_events():
    events = Event.query.all()
    return render_template('admin/events_list.html', events=events)


@app.route('/admin/orgs/<int:org_id>/events', methods=['GET'])
def admin_events_org(org_id):
    org = AppUser.query.get(org_id)
    events = org.events
    return render_template('admin/org_events.html', org=org, events=events)


@app.route('/admin/events/<int:id>')
def admin_event_details(id):
    event = Event.query.get(id)
    return render_template('admin/event_details.html', event=event)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = AppUser.query.filter_by(name=form.name.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            if user.is_admin:
                return redirect(url_for('admin_index'))
            return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/registration', methods=['GET', 'POST'])
def regist():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = AppUser()
        user.name = form.name.data
        user.subject = form.subject.data
        user.city = form.city.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)


@app.route('/api/events', methods=['GET'])
def get_events():
    return '', 202


@app.route('/api/events/<int:id>', methods=['GET'])
def get_event_by_id():
    return '', 202
