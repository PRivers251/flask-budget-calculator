from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    singleWeeklyExpenses = db.relationship
    password = db.column(db.String(60), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'