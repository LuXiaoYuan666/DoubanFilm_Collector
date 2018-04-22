# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     MongodbClient.py
   Description :  获取配置信息
   Author :       Lu Xiao Yuan
   date：          2018/4/18
-------------------------------------------------

"""

import sys
sys.path.append("..")
from pymongo import MongoClient
from ConfigGetter import getConfig


class MongodbClient(object):
    def __init__(self, name):
        self.name = name
        self.client = MongoClient(getConfig('DB','host'), int(getConfig('DB','port')))
        self.db = self.client[getConfig('Proxy','DBName')]

    def put(self, proxy):
        if self.db[self.name].find_one({'proxy': proxy}):
            return None
        else:
            self.db[self.name].insert({'proxy': proxy})

    def delete(self, value):
        self.db[self.name].remove({'proxy': value})

    def getAll(self):
        return [i['proxy'] for i in self.db[self.name].find({},{'proxy':1})]

    def clean(self):
        self.client.drop_database('proxy')

    def delete_all(self):
        self.db[self.name].remove()




if __name__ == "__main__":
    test = MongodbClient('database')
    test.put('kk')


