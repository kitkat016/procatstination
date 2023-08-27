from flask import Flask, render_template, flash, request, g, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

# Initialse The App
app = Flask(__name__, static_url_path='/procatstination/static')
app.config['SECRET_KEY'] = "key"
app.debug = True


# Initialise The Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///character.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Spider7@localhost/characters'
db = SQLAlchemy(app)

# Create Database Model
class User(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20), primary_key=True)
    strength_stat = db.Column(db.Integer, nullable=False, default=0)
    intelligence_stat = db.Column(db.Integer, nullable=False, default=0)
    wisdom_stat = db.Column(db.Integer, nullable=False, default=0)

# Create a Form Class
class UserForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])

# Function to return a string when something is added to the database
def __repr__(self):
    return '<Name %r>' % self.id

#Updating the Database
@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    character = UserForm()
    character_to_update = User.query.get_or_404(id)
    if request.method == "POST":
        character_to_update.name = request.form['name']
        character_to_update.strength_stat = request.form['strength']
        character_to_update.intelligence_stat = request.form['intelligence']
        character_to_update.wisdom_stat = request.form['wisdom']
        try:
            db.session.commit()
            flash('Character updated successfully')
            return render_template('update.html',
                                   character = character,
                                   character_to_update = character_to_update)
        except:
            db.session.commit()
            flash('An error occured updating')
            return render_template('update.html',
                                   character = character,
                                   character_to_update = character_to_update)
    else:
        return render_template('update.html',
                                character = character,
                                character_to_update = character_to_update)


@app.route("/")
def home():
    return render_template('login.html',
                           form=UserForm())

@app.route("/login", methods=['GET', 'POST'])
def login():
    character = UserForm()
    if character.validate_on_submit():
        new_username = character.username.data
        new_password = character.password.data
        my_character = User.query.filter_by(username=character.username.data,
                                             password=character.password.data).first()
        if my_character is None:
            new_character = User(username=new_username,
                                    password=new_password)
            db.session.add(new_character)
            db.session.commit()           
    my_character = User.query.filter_by(username=character.username.data,
                                             password=character.password.data).first()
    return render_template("index.html", my_character=my_character)

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/strength", methods=['GET', 'POST'])
def strength():
    character = UserForm
    username = character.username.data
    password = character.password.data
    my_character = my_character = User.query.filter_by(username=username,
                                             password=password).first()
    return render_template('strength.html', my_chararacter = my_character)

@app.route("/strength_update", methods=['GET','POST'])
def strength_updated():
    print("bingo")
    character = UserForm()
    username = character.username.data
    password = character.password.data
    character_to_update = User.query.get_or_404(username, password)
    character_to_update.strength_stat += 1
    try:
        db.session.commit()
        flash('Character updated successfully')
    except:
        flash('An error occured updating')
    return render_template('strength.html')