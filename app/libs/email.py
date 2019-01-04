# -*- coding: utf-8 -*-
from flask_mail import Message

from app import mail

_Author_ = 'BUPPT'


def send_email():
    msg = Message("测试邮件", sender='shixintianbupt@163.com', body='Test', recipients=['sxt8429@163.com'])
    mail.send(msg)
