# -*- coding: utf-8 -*-
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app import mail

_Author_ = 'BUPPT'


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_email(to, subject, template, **kwargs):
    # msg = Message("测试邮件", sender='shixintianbupt@163.com', body='Test', recipients=['sxt8429@163.com'])
    # mail.send(msg)
    msg = Message('[鱼书]' + ' ' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
