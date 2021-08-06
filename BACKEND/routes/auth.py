from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask_user import roles_required
from werkzeug.security import generate_password_hash, check_password_hash
import models.Usuario
from app import db


from forms.login import LoginForm
from forms.register import RegisterForm

from functools import wraps


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = models.Usuario.User.query.filter_by(email=form.email.data).first()
        
        if user:
            if check_password_hash(user.password, form.password.data):

                login_user(user, remember=form.remember.data)
                flash('Login realizado com sucesso :D')
                
                if user.access == 1:
                    user.is_admin()
                    #return redirect(url_for('dash.dashboard'))
                    return redirect(url_for('admin_dash.dashboard'))
                                
                
                return redirect(url_for('dash.dashboard'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))



@auth.route('/signup', methods=['GET', 'POST'])
#@login_required
def signup():
    form = RegisterForm()
    
    print(form.username)

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        
        new_user = models.Usuario.User(username=form.username.data, phone=form.phone.data,  email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        #return redirect(url_for('dash.dashboard'))
        return redirect(url_for('dash.dashboard'))
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)



def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                # Redirect the user to an unauthorized notice!
                return "You are not authorized to access this page"
            return f(*args, **kwargs)
        return wrapped
    return wrapper  