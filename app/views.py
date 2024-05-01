from flask import Blueprint, session, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user,login_user
from . import db
from .models import *
from flask import current_app as app
from .wtf_forms import Register_Form,Login_Form
from werkzeug.security import check_password_hash, generate_password_hash

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def index():
    return render_template('index.html')
    
@views.route('/login', methods=['POST','GET'])
def login():
    login_form= Login_Form()
    register_form= Register_Form()
    if request.method=='POST':
        if login_form.validate_on_submit():
            print('login form submitted')
            user_data = Users.query.filter_by(username = login_form.username.data).first()
            if user_data:
                if check_password_hash(user_data.password, login_form.password.data):
                    flash('successfully logged in')
                    login_user(user_data, remember=True)
                    return redirect(url_for('views.index'))
                else:
                    flash('Wrong Password')
            else:
                flash('No user Available')
        if login_form.errors and login_form.errors!={}:
            print('login error occured')
            for error in login_form.errors.values():
                print(f'the error in register is {error}')
                flash(f'the error in register is {error}')

        if register_form.validate_on_submit():
            print('register form submitted')
            user_to_add=Users(username= register_form.username.data,
                            email= register_form.email.data,
                            password= generate_password_hash(register_form.password.data))
            db.session.add(user_to_add)
            db.session.commit()
            login_user(user_to_add, remember=True)
            return redirect(url_for('views.index'))
        if register_form.errors and register_form.errors!={}:
            print('register error occured')
            for error in register_form.errors.values():
                print(f'the error in register is {error}')
                flash(f'the error in register is {error}')

    return render_template('login.html',register_form=register_form, login_form=login_form)



