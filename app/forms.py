from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class CompanyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    electricity = IntegerField('Electricity', validators=[DataRequired()])
    natural_gas = IntegerField('Natural Gas', validators=[DataRequired()])
    fuel = IntegerField('Fuel', validators=[DataRequired()])
    waste = IntegerField('Waste', validators=[DataRequired()])
    recycled_percent = IntegerField('Recycled Percent', validators=[DataRequired()])
    business_travels = IntegerField('Business Travels', validators=[DataRequired()])
    fuel_efficiency = IntegerField('Fuel Efficiency', validators=[DataRequired()])
