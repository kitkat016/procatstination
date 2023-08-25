from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialse The App
app = Flask(__name__)

# Initialise The Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///character.db'
db = SQLAlchemy(app)

# Create Database Model
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(20), nullable=False)
    # strength_stat = db.Column(db.Integer, nullable=False)
    # intelligence_stat = db.Column(db.Integer, nullable=False)
    # wisdom_stat = db.Column(db.Integer, nullable=False)

# Function to return a string when something is added to the database
def __repr__(self):
    return '<Name %r>' % self.id

with app.app_context():
    db.create_all()

@app.route("/")

def home():
    return "Testing"