from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = '0f1622fa0615aec88830a4d5c3935321'   #Security Layer
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from webapp import routes

