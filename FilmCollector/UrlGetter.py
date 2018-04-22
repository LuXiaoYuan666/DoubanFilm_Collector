# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     UrlGETTER.py
   Description :  获得所有电影列表
   Author :       Lu Xiao Yuan
   date：          2018/4/17
-------------------------------------------------

"""
from PageDownloader import download_page
from PageParser import get_page
from ConfigGetter import getConfig

def get_filmURLs(num_page):
    type = getConfig('FilmCollector', 'type')
    url_nopage = 'https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=%E7%94%B5%E5%BD%B1&genres='+type+'&start='
    film_URLs = []
    for i in range(num_page):
        url = url_nopage + str(i * 20)
        doc = download_page(url)
        film_URL = get_page(doc)
        print('第' + str(i + 1) + '页电影解析成功，有' + str(len(film_URL)) + '部电影')
        if len(film_URL)==0:
            print('第'+str(i)+ '页部电影没有电影啦')
            break
        film_URLs = film_URL+film_URLs
    return film_URLs

if __name__ == '__main__':
    get_filmURLs(1)