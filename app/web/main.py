from flask import render_template
from flask_login import login_required, current_user

from app.models.gift import Gift
from app.models.user import User
from app.view_models.book import BookViewModel
from . import web

__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
@login_required
def personal_center():
    user = current_user.summary
    return render_template('personal.html', user=user)
