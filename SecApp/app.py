from flask import Flask, render_template, request, redirect, url_for #a micro web framework,  renders html template, http requests, redirects, generates url
from flask_sqlalchemy import SQLAlchemy #for database interactions
from flask_bcrypt import Bcrypt #for password hashing
from flask_wtf import FlaskForm, CSRFProtect #for form handling and CSRF protection
from wtforms import StringField, PasswordField  #text inputs and password input
from wtforms.validators import InputRequired, Email, Length, EqualTo #ensure field is field, valdates email format, checks input lenth, compares input(password confirmation)
from flask_migrate import Migrate #initialize Flask-Migrate



app = Flask(__name__) #create a flask application instance
app.config['SECRET_KEY'] = 'secret_key' #change this to your secrete key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #creates the database


db = SQLAlchemy(app) #initialize SQLAlchemy with the Flask app
bcrypt = Bcrypt(app) #initialize Flask-Bcrypt with the Flask app
csrf = CSRFProtect(app) #enable CSRF token
migrate = Migrate(app, db) #initialize Migrate  with the Flask app and SQLAlchemy database


#Creating a database users table model object
class Users(db.Model): #define a Users model using SQLAchemy
    __tablename__ = 'users'#defines a tablename
    id = db.Column(db.Integer, primary_key=True) #unique integer identifier.
    username = db.Column(db.String(80), unique=True, nullable=False) #unique string
    email = db.Column(db.String(120), unique=True, nullable=False) #unique string
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email, password): #initializes a new user instance hashing the password
        self.username = username 
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')#Encrypts password for password protection

#creating a login form object
class LoginForm(FlaskForm):  #define a login form using Flask-WTF
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=80)]) #text inputs with validators
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=120)]) #password input with valdators

#creating a registration form object
class RegisterForm(FlaskForm): #define a registration form using Flask-WTF
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=80)]) #text inputs with validators
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)]) #text input with validators for email
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=120), EqualTo('confirm_password')]) #password input with valdators
    confirm_password = PasswordField('Confirm Password') #password input with valdators

#Defining the path to the pages and Redirection
@app.route('/') #home page
def index():
    return render_template('index.html')

#Routes
@app.route('/login', methods=['GET', 'POST']) #login page
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])#register page
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = Users(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/dashboard') #dashboard
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=False) #starts a debuger if set to True

#do this before running the app.py file
#Open your terminal in the project directory
#Run:
#python -m flask db init
#python -m flask db migrate
#python -m flask db upgrade
