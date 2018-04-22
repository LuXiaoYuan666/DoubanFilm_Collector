# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     ConfigParser.py
   Description :  获取配置信息
   Author :       Lu Xiao Yuan
   date：          2018/4/18
-------------------------------------------------

"""

import configparser

def getConfig(section, key):
	#获取配置信息
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Administrator\Desktop\FilmCollector V1\config.ini',encoding='utf8')
    return config.get(section, key)


if __name__ == '__main__':
    c = getConfig('DB', 'type')
    print(c)
