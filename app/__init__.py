from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from datetime import datetime , timedelta
from flask_migrate import Migrate

from sqlalchemy import create_engine

db=SQLAlchemy()
DB_NAME='database.db'

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['SECRET_KEY']='idhu_epdi_irukku-->indha_secret_key'

    db_path = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(db_path, DB_NAME)}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    migrate = Migrate(app, db)

    from . import models
    from .models import Users,Workouts
    models.db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'views.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))
    
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    
    if not os.path.exists(os.path.join(app.instance_path, DB_NAME)):
        with app.app_context():
            db.create_all()
        print('Created Database!')
    
    return app    