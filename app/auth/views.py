from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,logout_user,login_required
from . import auth
from ..models import Writer
from .forms import LoginForm,RegistrationForm
from .. import db
from ..email import mail_message


@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        writer = Writer.query.filter_by(email = form.email.data).first()
        if writer is not None and writer.verify_password(form.password.data):
            login_user(writer,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password')

    title = 'Blog App Login'
    return render_template('auth/login.html', title = title, login_form = form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        writer = Writer(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(writer)
        db.session.commit()

        return redirect(url_for('auth.login'))
        title = 'New Account'
    return render_template('auth/register.html', registration_form = form)
