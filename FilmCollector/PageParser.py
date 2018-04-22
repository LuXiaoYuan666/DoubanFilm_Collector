# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     PageParser.py
   Description :  json page parser
   Author :       Lu Xiao Yuan
   date：          2018/4/15
-------------------------------------------------

"""

import json

def get_page(doc):
    try:
        #获取电影列表的所有电影链接
        data = json.loads(doc)
        film = data['data']
        url_list = []
        print('page成功载入')
        for n in film:
            url = n['url']
            url_list = [url] + url_list
        return url_list
    except Exception as e:
        print(e)