# coding:utf-8
# @Time     :   2020/5/5 22:23
# @Author   :   Wangkui
# @File     :   scale_forms.py
# @Software :   PyCharm
# @Desc     :
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddScaleForm(FlaskForm):
    main_title = StringField('大标题', validators=[DataRequired()])
    sub_title = StringField('副标题', validators=[DataRequired()])
    desc = TextAreaField('说明')
    need_know = TextAreaField('须知')
    instruction = TextAreaField('指导语')
    topic_explanation = TextAreaField('题目解释')
    topic_interpretation = TextAreaField('题目解读')
    causes_performance = TextAreaField('成因与表现')
    suggest  = TextAreaField('建议')
    submit = SubmitField('提交')