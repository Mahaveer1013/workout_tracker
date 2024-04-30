from flask import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

from sqlalchemy import create_engine

db=SQLAlchemy()
DB_NAME='database.db'
