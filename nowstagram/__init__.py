# -*- encoding=UTF-8 -*-

from  flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
app.config.from_pyfile('app.conf')
db = SQLAlchemy(app)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.secret_key = 'zjs'
login_manager=LoginManager(app)

login_manager.login_view = '/regloginpage/'
from nowstagram import views, models