from flask import Flask, render_template, flash, request, session, url_for, redirect, g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

# Initialse The App
app = Flask(__name__)
app.config['SECRET_KEY'] = "key"

# Initialise The Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///character.db'
#password after root: must change
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Spider7@localhost/characters'
db = SQLAlchemy(app)

# Create Database Model
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    strength_stat = db.Column(db.Integer, nullable=False, default=0)
    intelligence_stat = db.Column(db.Integer, nullable=False, default=0)
    wisdom_stat = db.Column(db.Integer, nullable=False, default=0)

# Create a Form Class
class UserCharacter(FlaskForm):
    name = StringField("name", validators=[DataRequired()])

# Function to return a string when something is added to the database
def __repr__(self):
    return '<Name %r>' % self.username

# Called before page requests, if user is logged in, g may be used in html without need to pass in User
@app.before_request
def before_request():
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_ud'])
        g.user = user

# Initial Page
@app.route("/", methods=['GET', 'POST'])
def onboarding():
    if request.method == "POST":
        session.pop('user_id', None)
        r_username = request.form['username']
        r_password = request.form['password']

        user = User.query.filter_by(username=r_username,
                                         password=r_password).first()
        if user is None:
            flash("Incorrect Username or Password")
            return redirect(url_for(''))
        else:
            session['user_id'] = user.id
            return redirect(url_for('<string:username>')) 
    return render_template('onboarding.html')

# Signing up for a character
@app.route("/NewUser", methods=['GET', 'POST'])
def new_character():
    character = UserCharacter()
    if character.validate_on_submit():
        user = User.query.filter_by(username=character.username.data).first()
        if user is None:
            user = User(username=character.username.data,
                             password=character.password.data)
            db.session.add(user)
            db.session.commit()
            character.username.data = ''
            character.password.data = ''
            flash("Character Created Successfully")
        else:
            flash("This Username is Taken")
            return render_template('register.html')
    return render_template("index.html")

# Main Page
@app.route("/<username>")
def home():
    return render_template('index.template')
    
# Going to strength page
@app.route("/<username>/strength")
def strength():
    return render_template('strength.html')

# Going to intelligence page
@app.route("/<username>/intelligence")
def intelligence():
    return render_template('intelligence.html')

# Going to wisdom page
@app.route("/<username>/wisdom")
def wisdom():
    return render_template('wisdom.html')



# Adding to the Database
@app.route("/character/add", methods=['GET', 'POST'])
def add_user():
    name = None
    character = UserCharacter()
    if character.validate_on_submit():
        user = User.query.filter_by(username=character.username.data).first()
        if user is None:
            user = User(name=character.name.data)
            db.session.add(user)
            db.session.commit()
        name = character.name.data
        character.name.data = ''
        flash("Character Created Successfully")
    my_character = User.query.filter_by(username=character.username.data)
    return render_template("add_character.html",
                           character=character,
                           name=name,
                           my_character=my_character)

#Updating the Database
@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    character = UserCharacter()
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

