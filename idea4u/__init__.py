from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment



# Application Basics
app = Flask('idea4u')
app.config.from_pyfile('settings.py')
# app.debug = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
moment = Moment(app)

from idea4u import views, commands
