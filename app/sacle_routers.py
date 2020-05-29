# coding:utf-8
# @Time     :   2020/5/5 22:12
# @Author   :   Wangkui
# @File     :   sacle_routers.py
# @Software :   PyCharm
# @Desc     :
from flask import render_template
from app.scale_forms import AddScaleForm
from . import app


@app.route('/scale')
def scale():
    add_scale_form = AddScaleForm()
    return render_template('assessment/scale_main.html', title='主页', add_scale_form=add_scale_form)

