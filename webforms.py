from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

# 创建表单类
# class UserForm(FlaskForm):
#     id = StringField("请输入你的id", validators=[DataRequired()])
#     userName = StringField("请输入你的名字", validators=[DataRequired()])
#     password = PasswordField("请输入你的密码", validators=[DataRequired()])
#     email = StringField("请输入你的邮件", validators=[DataRequired()])
#     identityNumber = StringField("请输入你的身份数字", validators=[DataRequired()])
#     location = StringField("请输入你的地址", validators=[DataRequired()])
#     verificationCode = StringField("请输入邮箱验证码", validators=[DataRequired()])
#     submit = SubmitField("submit")

# login的表单
class LoginForm(FlaskForm):
    id = StringField("请输入用户id", validators=[DataRequired()])
    password = PasswordField("请输入用户密码", validators=[DataRequired()])
    submit = SubmitField("提交")

# signUp的表单
class SignupForm(FlaskForm):
    name = StringField("请输入用户名", validators=[DataRequired()])
    password = PasswordField("请输入用户密码", validators=[DataRequired()])
    submit = SubmitField("提交")
# 反馈后台信息
class FeelingSend(FlaskForm):
    message = StringField("请输入您想反馈的内容", validators=[DataRequired()])
    contact = StringField("请输入您的联系方式", validators=[DataRequired()])
    submit = SubmitField("提交")

# BooleanField
# DateField
# DateTimeField
# DecimalField
# FileField
# HiddenField
# MultipleField
# FieldList
# FloatField
# FormField
# IntegerField
# PasswordField
# RadioField
# SelectField
# SelectMultipleField
# SubmitField
# StringField
# TextAreaField

## Validators
# DataRequired
# Email
# EqualTo
# InputRequired
# IPAddress
# Length
# MacAddress
# NumberRange
# Optional
# Regexp
# URL
# UUID
# AnyOf
# NoneOf
