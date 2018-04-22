# coding: utf-8
"""
-------------------------------------------------
   File Name：    MongodbClient.py
   Description :  封装mongodb操作
   Author :       JHao netAir
   date：          2017/3/3
-------------------------------------------------
   Change Activity:
                   2017/3/3:
                   2017/9/26:完成对mongodb的支持
-------------------------------------------------
"""
__author__ = 'Maps netAir'

import sys
sys.path.append("..")
from pymongo import MongoClient
from ConfigGetter import getConfig


class MongodbClient(object):
    def __init__(self, name):
        self.name = name
        self.client = MongoClient(getConfig('DB','host'), int(getConfig('DB','port')))
        self.db = self.client.proxy

    def put(self, proxy):
        if self.db[self.name].find_one({'proxy': proxy}):
            return None
        else:
            self.db[self.name].insert({'proxy': proxy})

    def delete(self, value):
        self.db[self.name].remove({'proxy': value})

    def getAll(self):
        return [i['proxy'] for i in self.db[self.name].find({},{'proxy':1})]
        # return self.db[self.name].find({}, {'proxy': 1})

    def clean(self):
        self.client.drop_database('proxy')

    def delete_all(self):
        self.db[self.name].remove()




if __name__ == "__main__":
    test = MongodbClient('database')
    test.put('233')


