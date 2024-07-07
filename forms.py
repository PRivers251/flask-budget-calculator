from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField, FloatField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length  


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=6), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ExpenseForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(min=2, max=200)])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Expense')


class SingleExpenseForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(min=2, max=200)])
    date = DateField('Date', validators=[DataRequired()])
    recurring = BooleanField('Recurring')
    submit = SubmitField('Add Expense')


class IncomeForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(min=2, max=200)])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Expense')