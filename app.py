from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from forms import RegistrationForm, LoginForm, ExpenseForm, IncomeForm
from extensions import db, bcrypt, login_manager
from modelClasses.User import User
from modelClasses.Expenses import Expenses
from modelClasses.Income import Income
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        print("Form validated") #Debug Statement!!!!!
        user = User.query.filter_by(_email=form.email.data).first()
        print(f"User found: {user}") #Debug Statement!!!!!
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            print('Login successful') #Debug Statement!!!!!
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            print('Login unsuccessful') #Debug Statement!!!!!
            flash('Login unsuccessful. Please check email and password', 'danger')
    else:
        print("Form not validated")  #Debug Statement!!!!!      
    return render_template('login.html', form=form)




@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(_email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

    

if __name__ == '__main__':
    app.run(debug=True)