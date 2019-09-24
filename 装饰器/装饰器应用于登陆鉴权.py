# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/9 23:40


from functools import wraps

from flask import request, Flask, url_for, redirect

app = Flask(__name__)


def check_auth(username, password):
    return False


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return redirect(url_for('login'))   # 登陆不成功返回一个地址，例如登陆页面
        return f(*args, **kwargs)   # 鉴权没问题的，就走继续走原来的方法
    return decorated


def pring_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)
    return wrapper


@app.route('/')
def index():
    return 'Hello World'


@app.route('/info')
@requires_auth
def info():
    return '登陆成功'

"""
它的执行顺序是从里到外，最先调用最里层的装饰器，最后调用最外层的装饰器
上面的方法等价于
info = app.route('/info')(requires_auth(info))
"""

@app.route('/login')
def login():
    return '要登陆的哦'


app.run()