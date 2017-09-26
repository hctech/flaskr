# coding: utf-8

from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])
    photo = FileField('Your photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Image Only')])
    submit = SubmitField('Submit')


class AddUserForm(Form):
    name = StringField('Username', validators=[DataRequired()])
    role = SelectField('role', choices=[], coerce=int)
    submit = SubmitField(u'提交')


