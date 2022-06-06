from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length, Regexp, NumberRange


class InputForm(FlaskForm):
    items = StringField('Items', validators=[DataRequired(), Regexp("^[1-8](,[1-8])*$")])
    num_of_bins = IntegerField('Number of bins', validators=[InputRequired(), NumberRange(min=0, max=20)])
    algorithm = SelectField('Algorithm', choices=[('kk', 'kk'), ('ckk', 'ckk'), ('rnp', 'rnp'), ('irnp', 'irnp')])
    submit = SubmitField('Submit')
