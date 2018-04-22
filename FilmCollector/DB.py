# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     DB.py
   Description :  save data to MongoDb
   Author :       Lu xiao yuan
   date：          2018/4/18
-------------------------------------------------

"""

import pymongo
from ConfigGetter import getConfig


def GetType():

    # 获取电影类型，并转换为对应数据库的英文名
    TypeKey = getConfig('FilmCollector', 'type')
    TypeDict = {'剧情': 'FeatureFilm', '喜剧': 'ComedyFilm', '动作': 'AcitonFilm', '爱情': 'LoveFilm', '科幻': 'ScienceFilm',
                '悬疑': 'SuspenseFilm', '惊悚': 'PanicFilm', '恐怖': 'HorribleFilm', '犯罪': 'CrimeFilm',
                '同性': 'HomosexualFilm',
                '音乐': 'MusicFilm', '歌舞': 'DanceFilm', '传记': 'BiographyFilm', '历史': 'HistoryFilm', '战争': 'WarFilm',
                '西部': 'WestFilm', '奇幻': 'FantasyFilm', '冒险': 'AdventureFilm', '灾难': 'DisasterFilm', '情色': 'EroticaFilm',
                '武侠': 'ChinaGongfuFilm'
                }
    return TypeDict[TypeKey]


def save_db(results):
    #把爬到的数据存入数据库
    connection = pymongo.MongoClient(getConfig('DB', 'host'), int(getConfig('DB', 'port')))
    dbName = getConfig('DB', 'DBName')
    db = connection[dbName]
    collection = db[GetType()]

    if results == None:
        return None
    (a, b, c, d, e, f, g, h, i) = results
    one_film = {'title': a, 'year': b, 'type': c, 'star': d, 'director': e, 'actor': f, 'pp':
        g, 'time': h, 'film_page': i}
    collection.insert(one_film)
    collection.save(one_film)


if __name__ == '__main__':
    print(GetType())
    save_db([1, 2, 3, 4, 5, 6, 7, 8, 9])
