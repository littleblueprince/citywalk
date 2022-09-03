#########################
#### 基本配置 ####
########################

from flask import Flask, render_template, flash, url_for, request
from flask import redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from random import sample

from webforms import LoginForm, SignupForm, FeelingSend

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password123A.@47.101.197.145:3306/citywalk'  # 数据库地址
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "123456"

db = SQLAlchemy(app)  # 实例化的数据库

migrate = Migrate(app, db)

# 曼哈顿距离计算
import math


def calculate_distance(lon1, lat1, lon2, lat2):
    return (3.14159 * 6371000 / 180) * (
            abs(lon1 - lon2) * math.cos(math.radians((lat1 + lat2) / 2)) + abs(lat1 - lat2))


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


# 景点曼哈顿记录记录表
class Place_distance(db.Model, UserMixin):
    __tablename__ = "place_distance"
    id = db.Column(db.Integer, primary_key=True)  # id
    place_id1 = db.Column(db.Integer, nullable=False)  #
    place_id2 = db.Column(db.Integer, nullable=False)  #
    distance = db.Column(db.Float, nullable=False)  #


# 景点信息表格
class Place(db.Model):
    __tablename__ = "place"
    id = db.Column(db.Integer, primary_key=True)  # id
    name = db.Column(db.String(50), nullable=False)  # 景点名称
    latitude = db.Column(db.Float, nullable=False)  #
    longitude = db.Column(db.Float, nullable=False)  #
    ticket_price = db.Column(db.String(50), nullable=False)  # 门票费
    advice_time = db.Column(db.Float, nullable=False)  # 建议游玩时长
    fit_people = db.Column(db.Integer, nullable=False)  # 适用人群
    rest_entertainment = db.Column(db.Float, nullable=False)  # 休闲娱乐
    cultural_connotation = db.Column(db.Float, nullable=False)  # 文化内涵
    easy_health_care = db.Column(db.Float, nullable=False)  # 轻松养生
    youth_vitality = db.Column(db.Float, nullable=False)  # 青春活力
    wealth_city = db.Column(db.Float, nullable=False)  # 繁华城市
    history_native_culture = db.Column(db.Float, nullable=False)  # 历史人文
    local_customs_and_practices = db.Column(db.Float, nullable=False)  # 风土人情
    nature = db.Column(db.Float, nullable=False)  # 自然
    single_visit = db.Column(db.Float, nullable=False)  # 单次游玩
    multi_visit = db.Column(db.Float, nullable=False)  # 多次游玩
    single_one_play = db.Column(db.Float, nullable=False)  # 单人行
    family_play = db.Column(db.Float, nullable=False)  # 合家欢
    sharpness = db.Column(db.Float, nullable=False)  # 鲜明程度
    environment_grade = db.Column(db.Float, nullable=False)  # 环境评分
    natural_scenery = db.Column(db.Float, nullable=False)  # 自然风光
    history_culture = db.Column(db.Float, nullable=False)  # 历史文化
    commercial_vitality = db.Column(db.Float, nullable=False)  # 商业活力
    folk_characteristics = db.Column(db.Float, nullable=False)  # 民俗特色
    local_life = db.Column(db.Float, nullable=False)  # 当地生活
    random = db.Column(db.Float, nullable=False)  # 随机数
    transport = db.Column(db.Integer, nullable=False)  # 交通方式


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


'''
注册api
'''


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    result = request.values.to_dict()
    arr = result.get('arr')
    form = SignupForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, password=form.name.data)
        if user is not None:
            db.session.add(user)
            db.session.commit()
            flash('注册成功')
            form.name.data = ''
            form.password.data = ''
            return redirect(url_for('login'))
        else:
            flash('注册失败')
            form.name.data = ''
            form.password.data = ''
    return render_template('signup.html', form=form)


'''
登录api
'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=form.id.data).first()
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


@app.route('/home', methods=["GET"])
# @login_required
def home():
    return render_template("home.html")


'''
退出
'''


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login', msg='退出成功'))


@app.route('/test', methods=["GET"])
def test():
    return render_template("test.html")


@app.route('/api', methods=["GET", "POST"])
def api():
    return "sadasdasdada"


@app.route('/apiTest', methods=["GET", "POST"])
def apiTest():
    form = FeelingSend()
    return render_template("apiTest.html", form=form)


# 更新距离表
@app.route('/insertPlace', methods=["GET", "POST"])
def insert():
    places = Place.query.all()
    for place1 in places:
        for place2 in places:
            re = calculate_distance(place1.longitude, place1.latitude, place2.longitude, place2.latitude)
            print(re)
            place_dis = Place_distance(place_id1=place1.id, place_id2=place2.id, distance=re)
            db.session.add(place_dis)
            db.session.commit()
    return "更新完成"


# 弗洛伊德算法
def floyd(graph, parents):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    parents[i][j] = parents[k][j]  # 更新父结点


def get_path_num(i, j, parents):
    count = 0
    while i != j:
        j = parents[i][j]
        count = count + 1
    return count


def get_path_str(i, j, parents):
    s = str(i)
    d = j
    while i != parents[i][j]:
        j = parents[i][j]
        s = s + str(j)
    s = s + str(d)
    return s


# 根据主题获取推荐路线(不采用)
# @app.route('/get_routes_test', methods=["GET", "POST"])
# def get_routes_test():
#     points = Place.query.all()
#     theme1 = 0
#     theme2 = 1
#     theme3 = 0
#     theme4 = 1
#     theme5 = 0
#     point_choose = []
#     # 选点部分
#     for point in points:
#         g1 = 0.85 * (point.natural_scenery * theme1 +
#                      point.history_culture * theme2 +
#                      point.commercial_vitality * theme3 +
#                      point.folk_characteristics * theme4 +
#                      point.local_life * theme5)
#         g2 = -1000
#         if theme1:
#             g2 = max(g1, point.natural_scenery)
#         if theme2:
#             g2 = max(g2, point.history_culture)
#         if theme3:
#             g2 = max(g2, point.commercial_vitality)
#         if theme4:
#             g2 = max(g2, point.folk_characteristics)
#         if theme5:
#             g2 = max(g2, point.local_life)
#         if max(g2, g1) > 0:
#             point_choose.append(point)
#     # print(point_choose)
#     print("选点部分结束")
#     # 产生路径
#     # 维数
#     ids = []
#     for i in point_choose:
#         ids.append(i.id)
#     print(ids)
#     n = len(ids)
#     # 无穷大
#     inf = 9999999999
#     # 构图
#     graph = [[(lambda x: 0 if x[0] == x[1] else inf)([i, j]) for j in range(n)] for i in range(n)]
#     parents = [[i] * n for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             dis = Place_distance.query.filter_by(place_id1=ids[i], place_id2=ids[j]).first()
#             graph[i][j] = dis.distance
#     # print(graph)
#     floyd(graph, parents)
#     for i in range(1, 5):
#         # 获取连接最短的两个点
#         str = ''
#         cost = 1000000
#         for i in range(n):
#             for j in range(n):
#                 if get_path_num(i, j, parents) == 1:
#                     if cost > graph[i][j]:
#                         cost = graph[i][j]
#                         str = get_path_str(i, j, parents)
#         print("最终结果:")
#         print(str)
#         print(cost)
#     return "sadada"

from collections import defaultdict
from heapq import *
import random


# 根据主题获取推荐路线
@app.route('/get_routes', methods=["GET", "POST"])
def get_routes():
    points = Place.query.all()
    max_score = 0
    max_point = -1
    theme1 = 0
    theme2 = 1
    theme3 = 0
    theme4 = 1
    theme5 = 0
    point_choose = []
    # 选点部分
    for point in points:
        g1 = 0.85 * (point.natural_scenery * theme1 +
                     point.history_culture * theme2 +
                     point.commercial_vitality * theme3 +
                     point.folk_characteristics * theme4 +
                     point.local_life * theme5)
        g2 = -1000
        if theme1:
            g2 = max(g1, point.natural_scenery)
        if theme2:
            g2 = max(g2, point.history_culture)
        if theme3:
            g2 = max(g2, point.commercial_vitality)
        if theme4:
            g2 = max(g2, point.folk_characteristics)
        if theme5:
            g2 = max(g2, point.local_life)
        if max(g2, g1) > 0:
            if max_score < max(g1, g2):
                max_score = max(g1, g2)
                max_point = point.id
            point_choose.append(point.id)
    # print(point_choose)
    print("选点部分结束")
    # 产生路径
    # 维数
    edges_list = []
    edges_all = Place_distance.query.filter_by().all()
    for i in edges_all:
        edges_list.append(i)
    edges_list.sort(key=lambda edge: edge.distance)
    # print(edges_list)
    # print(point_choose)
    result = defaultdict(list)  # 注意：defaultdict(list)必须以list做为变量
    for k in range(3, 7):
        points_to_do = sample(point_choose, k)
        adjacent_dict = defaultdict(list)  # 注意：defaultdict(list)必须以list做为变量
        for i in edges_list:
            if i.place_id1 in points_to_do and i.place_id2 in points_to_do:
                adjacent_dict[i.place_id1].append((i.distance, i.place_id1, i.place_id2))
                adjacent_dict[i.place_id2].append((i.distance, i.place_id2, i.place_id1))
        # print(adjacent_dict)
        minu_tree = []  # 存储最小生成树结果
        num_items = len(points_to_do)
        random_index = random.randrange(num_items)
        visited = [points_to_do[random_index]]  # 存储访问过的顶点，注意指定起始点
        adjacent_vertexs_edges = adjacent_dict[points_to_do[random_index]]
        heapify(adjacent_vertexs_edges)  # 转化为小顶堆，便于找到权重最小的边
        while adjacent_vertexs_edges:
            weight, v1, v2 = heappop(adjacent_vertexs_edges)  # 权重最小的边，并同时从堆中删除。
            if v2 not in visited:
                visited.append(v2)  # 在used中有第一选定的点'A'，上面得到了距离A点最近的点'D',举例是5。将'd'追加到used中
                minu_tree.append((weight, v1, v2))
                # 再找与d相邻的点，如果没有在heap中，则应用heappush压入堆内，以加入排序行列
                for next_edge in adjacent_dict[v2]:  # 找到v2相邻的边
                    if next_edge[2] not in visited:  # 如果v2还未被访问过，就加入堆中
                        heappush(adjacent_vertexs_edges, next_edge)
        result[k-1].append(minu_tree)
    return result


@app.route("/testPost", methods=["POST", "GET"])
def post():
    dict = request.values.to_dict()
    arr = dict.get('arr')
    print(arr)
    return "成功"


@app.route("/navigate", methods=["POST", "GET"])
def navigate():
    return render_template('navigate.html')


@app.route("/get_data", methods=["POST", "GET"])
def get_data():
    places = Place.query.filter_by().all()
    data = []
    j = 0
    for i in places:
        j = j + 1
        b = {"longitude": i.longitude, "latitude": i.latitude}
        data.append(b)
    print(data)
    return "dasda"

@app.route("/get_data_test",methods=["GET","POST"])
def get_data_test():
    return render_template("showDataTest.html")

@app.route("/test_A",methods=["GET","POST"])
def test_A():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)
    # 开启debug模式
