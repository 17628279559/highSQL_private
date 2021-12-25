#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 snaketao. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2021-12-16 14:31
# @FileName: picture_inster.py
# @Desc    : insert picture to mysql
import requests
from lxml import etree
import appbk_sql
from fake_useragent import UserAgent
from random import choice
import os
import re
url = "https://www.douban.com/search?q={}"
requests.packages.urllib3.disable_warnings()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

#从mysql获取所有id和title
def get_name():
    sql = "select movieid,title from movies where url is null;"
    result = appbk_sql.mysql_com(sql)
    data = []
    for i in result:
      data.append([i['movieid'],i['title']])
    return data

#从豆瓣爬取每个电影的链接和图片链接并插入数据库
def function_insert_picture():
    ip_data = []
    with open(r"ip_av.txt") as ip:
        for i in ip:
            ip_data.append(i.strip())
    for item in get_name():
        if item[0]>2891 and item[0]<16000:
            while True:
                try:
                    iii = choice(ip_data)
                    s = requests.session()
                    s.keep_alive = False  # 关闭多余连接
                    data = s.get(url.format(item[1]).replace(' ','%20'), headers=headers,proxies={"https":iii},verify=False)
                except Exception as e:
                    ip_data.remove(iii)
                    print(e)
                    continue
                break
            html=etree.HTML(data.text)
            print(iii)
            data.close()
            try:
                name_url = html.xpath('//div[@class="result-list"][1]//a[@class="nbg"][1]/@href')[0]
                name_picture = html.xpath('//div[@class="result-list"][1]//a[@class="nbg"][1]/img/@src')[0]
                pattern = re.compile("%2Fsubject%2F([0-9]+)%2F")
                name_url = 'https://movie.douban.com/subject/'+ re.search(pattern, name_url)[1] + '/'
                sql = "UPDATE movies SET url='{}',picture='{}' WHERE movieid = {}".format(name_url,name_picture,item[0])
                print(item[0],'成功')
                appbk_sql.mysql_com(sql)
            except Exception as e:
                print(e)
    
if __name__ == '__main__':
    #get_name()
    #function_insert_picture()
    pass
