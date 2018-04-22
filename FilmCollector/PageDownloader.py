# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     PageDownlodaer.py
   Description :  PageDownlodaer
   Author :       Lu xiao yuan
   date：          2018/4/18
-------------------------------------------------

"""

import requests
import random
import time
import string


# 随机获取单个代理
def get_proxy():
    return requests.get("http://127.0.0.1:8888/get/").text


# 删除代理
def delete_proxy(proxy):
    requests.get("http://127.0.0.1:8888/delete/?proxy={}".format(proxy))


def download_page(url):
    """获取url地址页面内容"""

    # 获取随机ua
    user_agent_list = [
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; msn OptimizedIE8;ZHCN)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW6s4; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; Zune 4.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; OfficeLiveConnector.1.4; OfficeLivePatch.1.3; yie8)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; OfficeLiveConnector.1.3; OfficeLivePatch.0.0; Zune 3.0; MS-RTC LM 8)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; OfficeLiveConnector.1.3; OfficeLivePatch.0.0; MS-RTC LM 8; Zune 4.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)',
    ]
    ua = random.choice(user_agent_list)
    headers = {
        'User-Agent': ua
    }
    # 随机生成一个11位的cookie
    num = ''.join(random.sample(string.digits + string.ascii_letters, 11))
    cookie = {'bid': num, 'll': '"108296"'}

    while True:
        try:
            proxy = get_proxy()
            # 判断是否存在proxy
            if (proxy == 'no proxy!'):
                print('No proxy, keep waiting for 1 seconds.')
                time.sleep(1)
            else:
                data = requests.get(url, headers=headers,
                                    proxies={"http": "http://" + proxy, "https": "https://" + proxy}, cookies=cookie,
                                    timeout=2)
                if (data.status_code == 200):
                    print('获取页面成功')
                    return data.text
                raise Exception('Failure')
        except Exception as e:
                    print(e)
                    delete_proxy(proxy)
