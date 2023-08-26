from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

# Initialse The App
app = Flask(__name__)
app.config['SECRET_KEY'] = "key"

# Initialise The Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///character.db'
db = SQLAlchemy(app)

# Create Database Model
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    strength_stat = db.Column(db.Integer, nullable=False, default=0)
    intelligence_stat = db.Column(db.Integer, nullable=False, default=0)
    wisdom_stat = db.Column(db.Integer, nullable=False, default=0)

# Create a Form Class
class UserCharacter(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    strength_stat = IntegerField("strength", validators=[DataRequired()])
    intelligence_stat = IntegerField("intelligence", validators=[DataRequired()])
    wisdom_stat = IntegerField("wisdom", validators=[DataRequired()])

# Function to return a string when something is added to the database
def __repr__(self):
    return '<Name %r>' % self.id

@app.route("/character/add", methods=['GET', 'POST'])
def add_user():
    name = None
    character = UserCharacter()
    if character.validate_on_submit():
        user = Character.query.filter_by(id=character.id.data).first()
        if user is None:
            user = Character(name=character.name.data)
            db.session.add(user)
            db.session.commit()
        name = character.name.data
        character.name.data = ''
        flash("Character Created Successfully")
    my_character = Character.query.filter_by(id=character.id.data)
    return render_template("add_character.html",
                           character=character,
                           name=name,
                           my_character=my_character)

@app.route("/")

def home():
    return "Testing"