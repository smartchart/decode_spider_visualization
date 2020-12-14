# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:17:48 2020

@author: Administrator
"""


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from pyecharts.charts import HeatMap
from pyecharts import options as opts

s = StandardScaler()
data = pd.read_excel('info_movies.xls')[['rank','year','score','comment']]
column = data.columns.tolist()
data1 = s.fit_transform(data)
corr = abs(np.corrcoef(data1.T))
value = [[i, j, corr[i,j]] for i in range(4) for j in range(4)]
heatmap = HeatMap()
heatmap.add_xaxis(column)
heatmap.add_yaxis("相关性热力学图", column, value)
heatmap.set_global_opts(
        title_opts=opts.TitleOpts(title="豆瓣电影排行数据分析结果"),
        visualmap_opts=opts.VisualMapOpts(max_=1),
    )
heatmap.render('templates/corr.html')
