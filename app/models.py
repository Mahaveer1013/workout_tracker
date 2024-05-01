from flask_login import UserMixin
from . import db
from sqlalchemy import JSON
from sqlalchemy.orm import relationship
from datetime import datetime

curr_date=datetime.now()

workout_data = {
    'lunges': [25, 3],
    'pushups': [20,3],
    'pullups': [20,3],
}

Daily_Record = {
    '30-03-2005':{
        'lunges': [25, 3],
        'pushups': [20,3],
        'pullups': [20,3],
    }
}

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    date= db.Column(db.DateTime(timezone=True), default=curr_date)


class Workouts(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    date= db.Column(db.DateTime(timezone=True), default=curr_date)
    username = db.Column(db.String(150), nullable=False, unique=True)
    workout_data = db.Column(JSON, nullable=True)

class Daily_Record(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    record = db.Column(JSON, nullable=True)
    date= db.Column(db.DateTime(timezone=True), default=curr_date)
