# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     DetailPaser.py
   Description :  解析单个页面页面详情
   Author :       Lu Xiao Yuan
   date：          2018/4/17
-------------------------------------------------

"""

from lxml import etree
from DB import save_db
from datetime import datetime
from PageDownloader import download_page

def get_detail(film_page):
    # 获取每个电影的页面详情
    now = datetime.today().strftime('%y-%m-%d %H:%M')
    detail = download_page(film_page)
    Selector = etree.HTML(detail)
    try:
	
		#pp代表观看人数
		#titile代表电影名字
		#star代表电影评分
		#year代表年份
		#director代表导演
		#actor代表演员
		#group代表类型
		#time代表电影时长
		
        pp = int(Selector.xpath('//span[@property="v:votes"]/text()')[0])
        title = Selector.xpath('//span[@property="v:itemreviewed"]/text()')[0]
        star = float(Selector.xpath('//strong[@property="v:average"]/text()')[0])
        year = Selector.xpath('//*[@id="content"]/h1/span[2]/text()')[0][1:5]
        director = ','.join(Selector.xpath('//*[@rel="v:directedBy"]/text()'))
        actor = ','.join(Selector.xpath('//*[@ rel="v:starring"]/text()'))
        Group = ','.join(Selector.xpath('//*[@property="v:genre"]/text()'))
        time = ','.join(Selector.xpath('//*[@property="v:runtime"]/text()'))
        print(now + ' ' + title + '已经被成功解析')
        results = (title, year, Group, star, director, actor, pp, time, film_page)
		#存储在数据库
        save_db(results)
        print(now + ' ' + title + '已经被记入数据库')
    except Exception as e:
        print(e)
        print('电影爬虫失败，链接为' + film_page)



if __name__ == '__main__':
    get_detail('https://movie.douban.com/subject/26384741/?from=showing')
