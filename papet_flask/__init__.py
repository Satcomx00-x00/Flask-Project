from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://projet:projet@10.59.63.131:5432/projetV2'
app.config['SECRET_KEY'] = '54364565bb46fe5672f435FE657df31e'
db = SQLAlchemy(app)

from papet_flask import routes
