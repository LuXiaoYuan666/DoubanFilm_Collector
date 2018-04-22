# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     ProxyApi.py  
   Description :  
   Author :       Lu Xiao Yuan
   date：          2018/4/18
-------------------------------------------------

"""

import sys

sys.path.append('../')

from flask import Flask, jsonify, request

from ProxyManager import ProxyManager

app = Flask(__name__)

api_list = {
    'get': u'get an usable proxy',
    'get_all': u'get all proxy from proxy pool',
    'delete?proxy=127.0.0.1:8080': u'delete an unable proxy',
}


@app.route('/')
def index():
    return jsonify(api_list)


@app.route('/get/')
def get():
    proxy = ProxyManager().get()
    return proxy if proxy else 'no proxy!'


@app.route('/get_all/')
def getAll():
    proxies = ProxyManager().getAll()
    return jsonify(proxies)


@app.route('/delete/', methods=['GET'])
def delete():
    proxy = request.args.get('proxy')
    ProxyManager().delete(proxy)
    return 'success'

@app.route('/refresh/')
def refresh():
    ProxyManager().refresh()
    pass
    return 'success'

def run():
    app.run(host='127.0.0.1',port=8888)



if __name__ == '__main__':
    run()
