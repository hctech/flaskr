# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from .. models import User


class LoginForm(Form):
    email = StringField(
        'Email', validators=[
            DataRequired(), Length(
                1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login In')


class RegistrationForm(Form):
    email = StringField(
        'Email', validators=[
            DataRequired(), Length(
                1, 64), Email()])
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(
                1,
                64),
            Regexp(
                '^[A-Za-z0-9_.]*$',
                0,
                'Username must have only letters, numbers, dots or underscores')])
    password = StringField(
        'Password',
        validators=[
            DataRequired(),
            EqualTo(
                'password2',
                message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField()


    # 表单类还有两个自定义的验证函数，以方法的实行实现。如果表单类中定义了以validate_开头且后面跟着字段名的方法，
    # 这个方法就和验证函数一起调用

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered.")


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already use.")
