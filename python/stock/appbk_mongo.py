#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 snaketao. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2021-10-17 14:17
# @FileName: appbk_mongo.py
# @Desc    : appbk mongodb数据库访问
import datetime
from pymongo import MongoClient
import re
import platform

# 带选择数据库功能

# 数据库
# 带选择数据库功能
MONGO_URL = "mongodb://snaketao:2rgNHvRkGRvaySPw@39.105.159.127:27017/?authSource=admin"  # 默认端口
MONGO_DB = "highSQL"

"""
功能：连接数据
"""


def connect_mongo(MONGO_URL=MONGO_URL,MONGO_DB=MONGO_DB):
    try:
        client = MongoClient(MONGO_URL)
        db = client[MONGO_DB]
    except Exception as e:
        print("ERROR:", e)
        return '-1'

    return db

"""
功能：执行mongodb插入命令
"""
def insert_data(data,mongo_set,  MONGO_URL=MONGO_URL ,MONGO_DB=MONGO_DB):
    # 连接数据库
    db = connect_mongo(MONGO_URL)
    if db == '-1':
        return -1

    try:
        db[mongo_set].insert(data)
    except Exception as e:
        print("ERROR", e)
        return e



"""
功能：批量执行mongodb插入命令
"""
def insert_all_data(data,mongo_set,  MONGO_URL=MONGO_URL ,MONGO_DB=MONGO_DB):
    # 连接数据库
    db = connect_mongo(MONGO_URL)
    if db == '-1':
        return -1
    try:
        db[mongo_set].insert(data)
    except Exception as e:
        print("ERROR", e)
        return e



"""
功能：更新插入
"""
def insert_update_data(set_name, old_data, new_data,  MONGO_URL=MONGO_URL ,MONGO_DB=MONGO_DB):
    # 连接数据库
    db = connect_mongo(MONGO_URL)
    if db == '-1':
        return -1

    try:
        db[set_name].update(old_data,{'$set':new_data},multi=False)
    except Exception as e:
        print("ERROR", e)
        return e

"""
功能：执行mongodb查询语句
"""
def serach_data(query,mongo_set,projection = None, MONGO_URL=MONGO_URL ,MONGO_DB=MONGO_DB):
    # 连接数据库
    db = connect_mongo(MONGO_URL)
    if db == '-1':
        return -1

    try:
        if projection:
            return db[mongo_set].find(query, projection)
        else:
            return db[mongo_set].find(query)
    except Exception as e:
        print("ERROR", e)
        return e
    

if __name__ == "__main__":
    pass
