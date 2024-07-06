from extensions import db
from datetime import datetime

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    _amount = db.Column(db.Float, nullable=False)
    _description = db.Column(db.String(200), nullable=False)
    _date = db.Column(db.DateTime, nullable=False)
    _recurring = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Monthly_Expense {self.description}, {self.date}>'
    

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
            raise ValueError("Date must be a datetime object")
        self._date = value


    @property
    def recurring(self):
        return self._recurring
    

    @recurring.setter
    def recurring(self, value):
        if not isinstance(value, bool):
            raise ValueError("Recurring value must be a boolean.")
        self._recurring = value
    