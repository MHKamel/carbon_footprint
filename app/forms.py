from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired,NumberRange

class CompanyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    electricity = IntegerField('Electricity', validators=[DataRequired(),NumberRange(min=0)])
    natural_gas = IntegerField('Natural Gas', validators=[DataRequired(),NumberRange(min=0)])
    fuel = IntegerField('Fuel', validators=[DataRequired(),NumberRange(min=0)])
    waste = IntegerField('Waste', validators=[DataRequired(),NumberRange(min=0)])
    recycled_percent = FloatField('Recycled Percent', validators=[DataRequired(),NumberRange(min=0, max=1)])
    business_travels = IntegerField('Business Travels', validators=[DataRequired(),NumberRange(min=0)])
    fuel_efficiency = FloatField('Fuel Efficiency', validators=[DataRequired(),NumberRange(min=0, max=1)])
