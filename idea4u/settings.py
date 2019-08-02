import os
import sys

from idea4u import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
SQLALCHEMY_TRACK_MODIFICATIONS = False
