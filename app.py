#########################
#### 基本配置 ####
########################
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from flask import Flask, request, jsonify, Blueprint, render_template, flash, url_for
from flask import abort, redirect, session
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from sqlalchemy import extract, and_
from flask_mail import Mail, Message
from webforms import LoginForm,SignupForm
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password123A.@47.101.197.145:3306/citywalk'   # 数据库地址
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "123456"

db = SQLAlchemy(app)  # 实例化的数据库

migrate = Migrate(app, db)

########################
#### 数据库 ####
########################
# 定义了数据库表的模型

# 已经激活的学生的表
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # id
    password = db.Column(db.String(30), nullable=False)  # 用户密码，不能为空
    name = db.Column(db.String(25), nullable=False)  # 不能为空

    # create a string
    def __repr__(self):
        return '<id %r>' % self.id


# 先执行try块，出错则执行except，否则不执行
try:
    db.create_all()
except:  # 出错
    pass

# 登录控制
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# 管理查询id的表（用于出错加载时加载到正确的位置，保护机制）
@login_manager.user_loader
def load_user(user_id):
    if User.query.get(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id
        return curr_user

########################
#### api ####
########################
'''
主页，进入登录或者注册
'''
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def index1():
    return render_template("index.html")

'''
注册api
'''
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        user = User(name=form.name.data,password=form.name.data)
        if user is not None:
            db.session.add(user)
            db.session.commit()
            flash('注册成功')
            form.name.data=''
            form.password.data=''
            return redirect(url_for('login'))
        else:
            flash('注册失败')
            form.name.data = ''
            form.password.data = ''
    return render_template('signup.html',form=form)

'''
登录api
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(id=form.id.data).first()
        if user is not None and form.password.data == user.password:
            curr_user = User()
            curr_user.id = form.id.data
            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)
            flash("登陆成功")
            return redirect(url_for('index'))
        flash('密码错误或者账户错误')
    form.id.data = None
    form.password.data = ''
    return render_template('login.html',
                           form=form)

'''
个人主页
'''
@app.route('/home',methods=["GET"])
# @login_required
def home():
    return render_template("home.html")

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login', msg='退出成功'))

@app.route('/test',methods=["GET"])
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)
    # 开启debug模式