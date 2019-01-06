from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.libs.email import send_email
from app.models.base import db
from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.trade import MyTrades
from app.view_models.wish import MyWishes
from . import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishs(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gifts_counts(isbn_list)
    view_model = MyTrades(wishes_of_mine, gift_count_list)
    return render_template('my_wish.html', wishes=view_model.trades)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):

        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id

            db.session.add(wish)

    else:
        flash("这本书已添加至你的赠送清单或已存在于你的心愿清单，请勿重复添加")

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
@login_required
def satisfy_wish(wid):
    wish = Wish.query.get_or_404(wid)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        flash("你还没有上传此书")
    else:
        send_email(wish.user.email, "有人想送你一本书", 'email/satisfy_wish.html', wish=wish, gift=gift)
        flash("已向他/她发送了一份邮件，如果他/她接收你的赠送，你将受到一个鱼漂")
    return redirect(url_for('web.book_detail', isbn=wish.isbn))


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn=isbn, launched=False).first_or_404()
    with db.auto_commit():
        wish.delete()
    return redirect(url_for('web.my_wish'))
