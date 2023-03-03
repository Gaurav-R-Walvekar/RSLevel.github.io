from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField,FloatField


class AddNumbersForm(FlaskForm):
    num1 = FloatField('Closing Price: ')
    num2 = FloatField('Ratio:         ')
    submit = SubmitField('Calculate')
