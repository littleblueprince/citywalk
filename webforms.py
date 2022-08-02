from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


# 注册账户的表单
class usersForm(FlaskForm):
    email = StringField("请输入email", validators=[DataRequired()])
    name = StringField("请输入name", validators=[DataRequired()])
    password = PasswordField("请输入Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


# 创建注册邮箱的表单
# 邮箱判断是否注册过，然后通过验证码进入
class signupEmail(FlaskForm):
    email = StringField("请输入你的邮件", validators=[DataRequired()])
    verificationCode = StringField("请输入邮箱验证码", validators=[DataRequired()])


# 创建表单类
class UserForm(FlaskForm):
    id = StringField("请输入你的id", validators=[DataRequired()])
    userName = StringField("请输入你的名字", validators=[DataRequired()])
    password = PasswordField("请输入你的密码", validators=[DataRequired()])
    email = StringField("请输入你的邮件", validators=[DataRequired()])
    identityNumber = StringField("请输入你的身份数字", validators=[DataRequired()])
    location = StringField("请输入你的地址", validators=[DataRequired()])
    verificationCode = StringField("请输入邮箱验证码", validators=[DataRequired()])
    submit = SubmitField("submit")


# login的表单
class LoginForm(FlaskForm):
    id = StringField("id", validators=[DataRequired()])
    username = StringField("userName", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


# 一个验证码提交的表单
class stringSub(FlaskForm):
    code = StringField("code", validators=[DataRequired()])
    submit = SubmitField("Submit")


# student 学生登录的表单
class StudentLogin(FlaskForm):
    id = StringField("id", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


# 用户获取邮箱验证码
class EmailVerificationCode(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    submitEmail = SubmitField("submitEmail")


# 用户填写邮箱验证码
class IdentifyVerificationCode(FlaskForm):
    code = StringField("code", validators=[DataRequired()])
    submitCode = SubmitField("submitCode")


# 用户填写激活账户的表单
class confirmForm(FlaskForm):
    id = StringField("id", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
    submit = SubmitField("获取验证码")


# 提交验证码的表单
class codeSubForm(FlaskForm):
    code = StringField("code", validators=[DataRequired()])
    submit = SubmitField("submitCode")


# 重置密码的表单
class ResetPassword(FlaskForm):
    oldPassword = PasswordField("旧密码", validators=[DataRequired()])
    newPassword = PasswordField("新密码", validators=[DataRequired()])
    submit = SubmitField("submit")


# 实验报告表单
class ReportForm(FlaskForm):
    id = StringField("id", validators=[DataRequired()])
    submit = SubmitField("submit")


# Create A Search Form
class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")
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
