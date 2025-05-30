"""
Modelo de datos
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
if os.environ.get('TESTING'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
