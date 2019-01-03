# -*- coding: utf-8 -*-
from flask import Flask, current_app

_Author_ = 'BUPPT'

app = Flask(__name__)
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
with app.app_context():
    a = current_app
    d = current_app.config["DEBUG"]
    a