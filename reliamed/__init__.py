from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_migrate import Migrate
import os

app = Flask(__name__)
# Use DATABASE_URL from environment variables if available, otherwise fallback to local sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///reliamed.db')
app.config['SECRET_KEY'] = 'ef3cc4b50e1ffa8bbffa39dd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

migrate = Migrate(app, db)

from reliamed import routes