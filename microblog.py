# coding:utf-8
# @Time     :   2020/5/1 00:16
# @Author   :   Wangkui
# @File     :   microblog.py
# @Software :   PyCharm
# @Desc     :
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_sell_context():
    return {'db': db, 'User': User, 'Post': Post}