from extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.String(60), nullable=False)
    expenses = db.relationship('Expenses', backref='User', lazy=True)
    incomes = db.relationship('Income', backref='User', lazy=True)
    
    def __repr__(self):
        return f'<User {self.email}>'
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email cannot be empty.")
        self._email = value

    @property
    def password(self):
        return self._password
    

    @password.setter
    def password(self, value):
        if not value:
            raise ValueError("Password cannot be empty.")
        self._password = value