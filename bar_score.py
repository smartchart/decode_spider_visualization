# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:54:45 2020

@author: Administrator
"""

from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd

data = pd.read_excel('info_movies.xls')
score = data['score'].value_counts().sort_index()
x = score.index.tolist()
y = score.tolist()
bar = Bar()
bar.add_xaxis(x)
bar.add_yaxis('电影评分', y)
bar.set_global_opts(
    title_opts={'text': "电影评分分布", 'subtext': "来源于豆瓣电影top250排名"},
    brush_opts=opts.BrushOpts(),
    toolbox_opts=opts.ToolboxOpts(),
    datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
    tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    visualmap_opts=opts.VisualMapOpts(max_=50)
)
bar.render("templates/bar_score.html")
