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
import requests
import appbk_sql
from lxml import etree
from urllib import request
import time
import re
path = r'D:\\img\\'
path_imdb = r'E:\\img_imdb\\'

#from httplib2 import socks    #下载图片设置代理
#import socket
#socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, "127.0.0.1", 1080)
#socket.socket = socks.socksocket
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}


#从mysql获取所有id和图片链接
def get_movieid_and_picture():
    sql = "select movieid,picture from movies where picture is not null and pic is null;"
    result = appbk_sql.mysql_com(sql)
    data = []
    for i in result:
      data.append([i['movieid'],i['picture']])
    return data

#下载图片，存入本地，并更新数据库，在pic一栏存入"无意义路径",表示该movie已经下载图片
def function_download():
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

#从mysql获取所有id和imdbid
def get_id_link():
    sql = "SELECT a.movieid,imdbid FROM `links` a,`movies` b where a.movieid = b.movieid and pic_imdb is null;"
    result = appbk_sql.mysql_com(sql)
    data = []
    for i in result:
      data.append([i['movieid'],i['imdbid']])
    return data

#下载图片，存入本地，并更新数据库，在pic_imdb一栏存入"无意义路径",表示该movie已经下载图片
def function_download_picture_from_imdb():
    url_imdb="https://www.imdb.com/title/tt0{}/?ref_=fn_al_tt_1"
    opener = request.build_opener()
    opener.addheaders = ([("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"),])
    request.install_opener(opener)
    for item in get_id_link():
        try:
            data = requests.get(url_imdb.format(str(item[1])),headers=headers)
        except Exception as e:
            print(item[0],"下载出现问题",e)
        html=etree.HTML(data.text)
        data.close()
        try:
            imdb_picture_url = html.xpath(r'//div[@class="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img"]/img/@src')[0]
        except Exception as e:
            print(item[0],"xPath有问题",e)
        try:
            request.urlretrieve(imdb_picture_url,path_imdb+str(item[0])+'.jpg')
            sql = "UPDATE movies SET pic_imdb='{}' WHERE movieid = {}".format(str(item[0])+'.jpg',item[0])
            print(item[0],"下载成功")
            appbk_sql.mysql_com(sql)
        except Exception as e:
            print(item[0],"下载有问题",e)


if __name__ == '__main__':
    #function_download()
    #function_download_picture_from_imdb()
    pass