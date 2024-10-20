
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length


class CompanyForm(FlaskForm):

    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=3, max=100)])
    electricity = IntegerField('Electricity', validators=[InputRequired()])
    natural_gas = IntegerField('Natural Gas', validators=[InputRequired()])
    fuel = IntegerField('Fuel', validators=[InputRequired()])
    waste = IntegerField('Waste', validators=[InputRequired()])
    recycled_percent = IntegerField('Recycled Percent', validators=[InputRequired()])
    business_travels = IntegerField('Business Travels', validators=[InputRequired()])
    fuel_efficiency = IntegerField('Fuel Efficiency', validators=[InputRequired()])