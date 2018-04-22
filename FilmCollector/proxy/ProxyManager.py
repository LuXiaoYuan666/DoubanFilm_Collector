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

import sys
import random

from MongodbClient import MongodbClient
import GetProxy
import requests
from ConfigGetter import getConfig


class ProxyManager(object):
    """
    ProxyManager
    """

    def __init__(self):
        self.db = MongodbClient(getConfig('Proxy','CollectionName'))

    def refresh(self):
        """
        fetch proxy into Db by ProxyGetter
        :return:
        """
        # fetch
        ProxyGetter = GetProxy.getProxy()
        # store
        for i in ProxyGetter:
            for x in i:
                print(x)
                self.db.put(x)

    def get(self):
        """
        return a useful proxy
        :return:
        """
        item = self.db.getAll()
        if item:
            return random.choice(item)
        return None

    def delete(self, proxy):
        """
        delete proxy from pool
        :param proxy:
        :return:
        """
        self.db.delete(proxy)

    def getAll(self):
        """
        get all proxy from pool as list
        :return:
        """
        item = self.db.getAll()
        return item


if __name__ == '__main__':
    pp = ProxyManager()
    pp.refresh()
