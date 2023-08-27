from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user2.db'  # Use your desired database URI
db = SQLAlchemy(app)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    strength_stat = db.Column(db.Integer, nullable=False, default=0)
    intelligence_stat = db.Column(db.Integer, nullable=False, default=0)
    wisdom_stat = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    #characters = db.relationship('Character', backref='user', lazy=True)  # Add this line

    def __repr(self):
        return '<Username %r>' % self.username

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Create default character stats for the new user
        default_character = Character(
              # Associate the character with the new user
            name='Default Character',
            strength_stat=0,
            intelligence_stat=0,
            wisdom_stat=0,
            user_id=new_user.id
        )
        
        db.session.add(default_character)
        db.session.commit()

        flash('Registration successful. You can now log in.')
        #return redirect(url_for('login'))
    


    return render_template('register.html', form=form)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('register') == 'register':
            return redirect(url_for('register'))
    elif request.method == 'GET':
        return render_template('index.html')
    
    
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
