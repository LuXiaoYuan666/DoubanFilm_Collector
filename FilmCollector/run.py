# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     run.py
   Description :   run the program
   Author :       Lu xiao yuan
   date：          2018/4/15
-------------------------------------------------

"""
import time
from multiprocessing.dummy import Pool as ThreadPool
from UrlGetter import get_filmURLs
from DetailPaser import get_detail
from ConfigGetter import getConfig


def main():
    start = time.time()
    pool = ThreadPool(4)
    page_num = int(int(getConfig('FilmCollector','number of films'))/20)
    film_URLs = get_filmURLs(page_num)
    pool.map(get_detail, film_URLs)
    end = time.time()
    lastT = int(end - start)
    print('总共耗时{}s'.format(lastT))


if __name__ == '__main__':
    main()
