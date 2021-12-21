#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 snaketao. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2021-10-21 12:21
# @FileName: insert_mongo.py
# @Desc    : insert data to mongodb
import appbk_mongo
import pandas as pd

def function_insert_movies():
    file1 = pd.read_csv(r'E:\BaiduNetdiskDownload\ml-latest\movies.csv')
    data = []
    for indexs in file1.index:
        sett = {}
        a = file1.loc[indexs].values[:]
        sett['movieid'] = int(a[0])
        sett['title'] = a[1]
        sett['genres'] = a[2].split('|')
        sett['tags'] = []
        data.append(sett)
    file2 = pd.read_csv(r'E:\BaiduNetdiskDownload\ml-latest\genome-scores.csv')
    file3 = pd.read_csv(r'E:\BaiduNetdiskDownload\ml-latest\genome-tags.csv')
    print(-1)
    file2.sort_values(['movieId','relevance'],  ascending=[True,False], inplace=True)
    grouped = file2.groupby(['movieId']).head(3)

    result = pd.merge(grouped, file3, how='inner', on='tagId',left_index=False, right_index=False, sort=False,suffixes=('_x', '_y'), copy=True)
    result.sort_values(['movieId','relevance'],  ascending=[True,False], inplace=True)
    print(-1)
    index = 0
    for i in result.index:
        sett = {}
        num = result.loc[i].values[:]
        sett['tagid'] = int(num[1])
        sett['relevance'] = float(num[2])
        sett['tag_name'] = num[3]
        while data[index]["movieid"] < int(num[0]):
            if index%100 == 0:
                print(index)
            index+=1
        data[index]['tags'].append(sett)

    appbk_mongo.insert_data(data,'movies')

def function_insert_users():
    file1 = pd.read_csv(r'E:\BaiduNetdiskDownload\ml-latest\users.csv')
    data = []
    i = 0
    for indexs in file1.index:
        a = file1.loc[indexs].values[:]
        sett = {}
        sett['userid'] = int(a[0])
        sett['gender'] = a[1]
        sett['name'] = a[2]
        sett['ratings'] = []
        data.append(sett)

    file2 = pd.read_csv(r'E:\BaiduNetdiskDownload\ml-latest\ratings.csv')
    
    for indexs in file2.index:
        sett = {}
        a = file2.loc[indexs].values[:]
        now_id = int(a[0])
        if now_id%1000 == 0:
            print(now_id)
        sett["movieid"]  = int(a[1])
        sett["rating"] = float(a[2])
        sett["timestamp"] = int(a[3])

        if now_id > 10532:
            break;
        data[now_id-1]['ratings'].append(sett)
            
    appbk_mongo.insert_data(data,'users')




if __name__=="__main__":
    #function_insert_movies()
    #function_insert_users()