# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     ConfigParser.py
   Description :  获取proxy
   Author :       Lu Xiao Yuan
   date：          2018/4/18
-------------------------------------------------

"""

import requests
import time
import sys

sys.path.append('..')
from ConfigGetter import getConfig

#请重写爬取proxy网页

def getProxy():
    while True:
        try:
            r = requests.get(
                'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=b29dcd38be954968b5bbf0ee804ffb32&count=10&expiryDate=5&format=1')
            # print (r.status_code)
            data = r.json()
        except:
            print('error')
        interval = int(getConfig('Proxy', 'interval'))
        time.sleep(interval)
        try:
            yield ['{}:{}'.format(row['ip'], row['port']) for row in data['msg']]  
			# 确保每个proxy都是 host:ip正确的格式就行
        except:
            print('没有有效proxy ip生成')


if __name__ == '__main__':
    print(next(getProxy()))
