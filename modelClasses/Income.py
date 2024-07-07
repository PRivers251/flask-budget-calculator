from extensions import db
from datetime import datetime

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _amount = db.Column(db.Float, nullable=False)
    _description = db.Column(db.String(200), nullable=False)
    _date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f'<Weekly_Income {self.description}: ${self.amount}>'

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if value <= 0:
            raise ValueError("Amount must be positive.")
        self._amount = value

    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Description cannot be empty.")
        self._description = value


    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Date must be a datetime object.")    