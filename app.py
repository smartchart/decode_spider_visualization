# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:34:48 2020

@author: Administrator
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home/bar_region')
def bar_region():
    return render_template('bar_region.html')


@app.route('/home/bar_score')
def bar_score():
    return render_template('bar_score.html')


@app.route('/home')
def home():
    return  '欢迎来到化工过程与大数据课堂'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
