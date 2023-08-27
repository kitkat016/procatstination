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
    password = db.Column(db.String(20), nullable=False)
    strength_stat = db.Column(db.Integer, nullable=False, default=0)
    intelligence_stat = db.Column(db.Integer, nullable=False, default=0)
    wisdom_stat = db.Column(db.Integer, nullable=False, default=0)
    cat_id = db.Column(db.Integer, nullable=False, default=0)
    outfit_id = cat_id = db.Column(db.Integer, nullable=False, default=1)

# Create a Form Class
class UserForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
    increase = IntegerField("increase")

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


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('login.html',
                           form=UserForm())

@app.route("/login", methods=['GET', 'POST'])
def login():
    character = UserForm()
    if character.validate_on_submit():
        new_username = character.username.data
        new_password = character.password.data
        my_character = User.query.filter_by(username=new_username,
                                             password=new_password).first()
        if my_character is None:
            new_character = User(username=new_username,
                                    password=new_password)
            db.session.add(new_character)
            db.session.commit()           
    my_character = User.query.filter_by(username=new_username,
                                             password=new_password).first()
    return render_template("index.html", my_character=my_character)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    user = UserForm()
    if user.validate_on_submit():
        username = user.username.data
        password = user.password.data
        new_user = User.query.filter_by(username=username,
                                        password=password).first()
        if new_user is None:
            create_user = User(username=username,
                            password=password)
            db.session.add(create_user)
            db.session.commit()
            new_user = User.query.filter_by(username=username,
                                            password=password).first()
            return render_template("index.html", my_character=new_user)
        flash("This username is already taken ):")

@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/strength", methods=['GET', 'POST'])
def strength():
    character = UserForm()
    username = character.username.data
    password = character.password.data
    my_character = User.query.filter_by(username=username,
                                             password=password).first()
    return render_template('strength.html', my_character=my_character)

@app.route("/strength_update", methods=['GET','POST'])
def strength_update():
    character = UserForm()
    username = character.username.data
    password = character.password.data
    increase = character.increase.data
    print(username)
    character_to_update = User.query.get_or_404(username)
    print(character_to_update)
    if request.method == "POST":
        character_to_update.strength_stat += increase
    try:
        db.session.commit()
        flash('Character updated successfully')
    except:
        db.session.commit()
        flash('An error occured updating')
    my_character = User.query.filter_by(username=username,
                                             password=password).first()
    return render_template('index.html', my_character = my_character)

@app.route("/intelligence", methods=['GET', 'POST'])
def intelligence():
    return render_template('intelligence.html')

@app.route("/wisdom", methods=['GET', 'POST'])
def wisdom():
    return render_template('wisdom.html')

@app.route("/dress", methods=['GET', 'POST'])
def dress():
    return render_template('dress.html')

@app.route("/cat", methods=['GET', 'POST'])
def cat():
    return render_template('cat.html')

@app.route("/buffcat", methods=['GET', 'POST'])
def buffcat():
    return render_template('buffcat.html')

@app.route("/bigbraincat", methods=['GET', 'POST'])
def bigbraincat():
    return render_template('intelligencecat.html')

@app.route("/wisdomcat", methods=['GET', 'POST'])
def wisdomcat():
    return render_template('wisdomcat.html')

@app.route("/indexx", methods=['GET', 'POST'])
def indexx():
    user = UserForm()
    print("akjfbgaskfhaslkfhnas")
    username = user.username.data
    password = user.password.data
    my_character = User.query.filter_by(username=username,
                                             password=password).first()
    return render_template('index.html', my_character = my_character)