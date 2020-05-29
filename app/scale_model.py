# coding:utf-8
# @Time     :   2020/5/5 22:12
# @Author   :   Wangkui
# @File     :   scale_model.py
# @Software :   PyCharm
# @Desc     :
from app import db


class AddScale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main_title = db.Column(db.String, index=True)
    sub_title = db.Column(db.String, index=True)
    desc = db.Column(db.String)
    need_know = db.Column(db.String)
    instruction = db.Column(db.String)
    topic_explanation = db.Column(db.String)
    topic_interpretation = db.Column(db.String)
    causes_performance = db.Column(db.String)
    suggest = db.Column(db.String)