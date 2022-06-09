from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length, Regexp, NumberRange

from run_prtpy_algo.objects.algorithm_response import get_algorithms_choices


class InputForm(FlaskForm):
    items = StringField('Items', validators=[DataRequired(), Regexp("\d+(?:,\d+)?")])
    num_of_bins = IntegerField('Number of bins', validators=[InputRequired(), NumberRange(min=0, max=20)])
    algorithm = SelectField('Algorithm', choices=get_algorithms_choices())
    submit = SubmitField('Submit')
