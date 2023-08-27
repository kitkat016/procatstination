from flask import Flask, render_template, flash, request
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
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    strength_stat = db.Column(db.Integer, nullable=False, default=0)
    intelligence_stat = db.Column(db.Integer, nullable=False, default=0)
    wisdom_stat = db.Column(db.Integer, nullable=False, default=0)

# Create a Form Class
class UserCharacter(FlaskForm):
    name = StringField("name", validators=[DataRequired()])

# Function to return a string when something is added to the database
def __repr__(self):
    return '<Name %r>' % self.id

# Adding to the Database
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

#Updating the Database
@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    character = UserCharacter()
    character_to_update = Character.query.get_or_404(id)
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
    return render_template('index.html')

@app.route("/strength")
def strength():
    return render_template('strength.html')

@app.route("/intelligence")
def intelligence():
    return render_template('intelligence.html')

@app.route("/wisdom")
def wisdom():
    return render_template('wisdom.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/dress")
def dress():
    return render_template('dress.html')

@app.route("/cat")
def cat():
    return render_template('cat.html')

@app.route("/buffcat")
def buffcat():
    return render_template('buffcat.html')

@app.route("/bigbraincat")
def bigbraincat():
    return render_template('intelligencecat.html')

@app.route("/wisdomcat")
def wisdomcat():
    return render_template('wisdomcat.html')