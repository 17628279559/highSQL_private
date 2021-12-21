#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 snaketao. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2021-12-21 11:12
# @FileName: picture_download.py
# @Desc    : download picture
import appbk_sql
from urllib import request
import time
import re
path = r'D:\\img\\'

#from httplib2 import socks
#import socket
#socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, "127.0.0.1", 1080)
#socket.socket = socks.socksocket
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}


def get_movieid_and_picture():
    sql = "select movieid,picture from movies where picture is not null and pic is null;"
    result = appbk_sql.mysql_com(sql)
    data = []
    for i in result:
      data.append([i['movieid'],i['picture']])
    return data
def function():
    data = get_movieid_and_picture()
    opener = request.build_opener()
    opener.addheaders = ([("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"),])
    request.install_opener(opener)
    for item in data:
        try:
            print(item)
            request.urlretrieve(item[1],path+str(item[0])+'.jpg')
            sql = "UPDATE movies SET pic='{}' WHERE movieid = {}".format(str(item[0])+'.jpg',item[0])
            appbk_sql.mysql_com(sql)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    function()
