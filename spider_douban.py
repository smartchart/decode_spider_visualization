# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:38:07 2020

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent

ua = UserAgent()

result = []
for i in range(10):
    headers = {"User-Agent": ua.random}
    url = 'https://movie.douban.com/top250?start={}&filter='.format(25 * i)
    r = requests.get(url, headers=headers).text
    soup = BeautifulSoup(r, "html.parser")
    for tag in soup.find_all('div', class_='item'):
        try:
            m_rank = int(tag.find('em').get_text())  # 排名
            m_director = tag.find('p').get_text().split('\n')[2].split('/')
            m_year = int(m_director[0].split()[0])  # 年份
            m_region = m_director[1].split()[0]  # 国家
            m_type = m_director[2].split()[0]  # 电影类型
            m_name = tag.find('span', class_='title').get_text()  # 电影名
            m_score = float(tag.find('span', class_='rating_num').get_text())  # 评分
            m_url = tag.find('a').get('href')
            m_comment = int(tag.find('div', class_='star').find_all('span')[3].get_text()[:-3])
            r = [m_rank, m_year, m_region, m_type, m_name, m_score, m_url, m_comment]
            result.append(r)
        except:
            pass
columns = ['rank', 'year', 'region', 'type', 'name', 'score', 'url', 'comment']
df = pd.DataFrame(result, columns=columns)
df.to_excel('info_movies.xls')
