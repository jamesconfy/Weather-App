from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CurrentWeatherForm(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Submit')