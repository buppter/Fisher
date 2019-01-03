from flask import render_template, request, redirect, url_for

from app.forms.register import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web

__author__ = '七月'


@web.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()

        redirect(url_for('web.login'))

    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        pass
    return render_template('auth/login.html', form={'data':{}})


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass