#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 snaketao. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2021-12-13 18:14
# @FileName: function_mongo.py
# @Desc    : query function by mongo
import appbk_mongo
from pymongo import MongoClient
import numpy as np
import datetime

#查询id对应的人看过的所有电影，并且输出每个电影最相关的前三个标签
def function_A(id):
	query = {'userid':id}
	projection = {'name':1,'ratings.movieid':1,'ratings.rating':1,'ratings.timestamp':1,'_id':0}
	result = appbk_mongo.serach_data(query,'users',projection)
	name = result[0]['name']
	data = []
	for item in result[0]['ratings']:
		tmp = {}
		tmp["movieid"]=item["movieid"]
		tmp["rating"]=item["rating"]
		tmp["timestamp"]=t1 = str(datetime.datetime.fromtimestamp(item["timestamp"]).strftime('%Y年%m月%d日 %H:%M:%S'))
		tmp["tags"] = []
		data.append(tmp)
	data = sorted(data,key=lambda x:x['timestamp'], reverse=True)
	index = 0
	res = appbk_mongo.serach_data({'movieid':{'$in':[i['movieid'] for i in data]}},'movies',{'movieid':1,'title':1,'tags':1,'_id':0})
	index = 0
	for item in res:
		while data[index]['movieid'] != item['movieid']:
			index+=1
		data[index]["tags"]=item['tags']
		index = 0
	
	for i in data:
		print(i,end="\n\n")

#查询含有关键字的电影
def function_B(key_word):
	sql = "SELECT title FROM `movies` where LOWER(title)  like LOWER('%{}%');".format(key_word)
	result_field = appbk_mongo.mysql_com(sql)
	for item in result_field:
		print(item)
	return result_field

#查询不同风格类型的最受欢迎的20部电影
def function_C(type_of_movie):
	sql = "select movie_title , average_rating , num_of_rating from `genres` where `genres`.genres = '{}';".format(type_of_movie)
	result_field = appbk_mongo.mysql_com(sql)
	#for item in result_field:
	#	print(item)
	return result_field

#查询不同性别最受欢迎的20部电影
def function_D(gender):
	sql = "SELECT title , average_rating , num_of_rating from gender_favourite where gender = '{}';".format(gender)
	result_field = appbk_mongo.mysql_com(sql)
	for item in result_field:
		print(item)
	return result_field

if __name__=="__main__":
	#function_A(51)
	#function_B("girls")
	#function_C("Animation")
	#function_D("Man")
	pass



