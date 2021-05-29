# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:03:18 2020

@author: Administrator
"""


from pyecharts import options as opts
from pyecharts.charts import Bar,Pie,Page
import pandas as pd

data = pd.read_excel('info_movies.xls')
score = data['region'].value_counts().sort_index()
x = score.index.tolist()
y = score.tolist()

bar = Bar()
bar.add_xaxis(x)
bar.add_yaxis('电影国家', y)
bar.set_global_opts(
    title_opts={'text': "电影国家分布", 'subtext': "来源于豆瓣电影top250排名"},
    brush_opts=opts.BrushOpts(),
    toolbox_opts=opts.ToolboxOpts(),
    datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
    tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    visualmap_opts=opts.VisualMapOpts(max_=120)
)

data_pair = [list(z) for z in zip(x, y)]
data_pair.sort(key=lambda x: x[1])

pie = Pie()
pie.add(
        series_name="电影国家分布",
        data_pair=data_pair[:],
        radius="70%",
        )
pie.set_global_opts(
        title_opts=opts.TitleOpts(title="电影国家分布饼状图"),
        legend_opts=opts.LegendOpts(orient="vertical",pos_left="5%",pos_top="20%"),
#        visualmap_opts=opts.VisualMapOpts(max_=120)
    )
pie.set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ))

page = Page(layout=Page.SimplePageLayout)
page.add(pie)
page.add(bar)
page.render('templates/test.html')