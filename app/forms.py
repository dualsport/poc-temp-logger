from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Optional


class TempForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    machine = StringField('Machine', validators=[DataRequired()])
    maintemp = DecimalField('Main Temperature', validators=[DataRequired()])
    auxtemp = DecimalField('Aux Temperature', validators=[Optional()])
    submit = SubmitField('Submit')
