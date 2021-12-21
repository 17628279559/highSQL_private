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

def function_B(key_word):
	pass
	
def function_C(type_of_movie):
	pass

def function_D(gender):
	pass

if __name__=="__main__":
	function_A(51)
	#function_B("girls")
	#function_C("Animation")
	#function_D("Man")




