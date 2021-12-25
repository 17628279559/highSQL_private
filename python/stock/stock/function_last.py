#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 snaketao. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2021-12-17 15:40
# @FileName: lasted_function.py
# @Desc    : query function by mysql
import appbk_sql
import appbk_mongo
import numpy as np
import json
import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import  csrf_exempt 


@csrf_exempt
def function_A(request):
	id = int(request.GET.get('userid',''))
	query = {'userid':id}
	projection = {'name':1,'ratings.movieid':1,'ratings.rating':1,'ratings.timestamp':1,'_id':0}
	result = appbk_mongo.serach_data(query,'users',projection)
	data = []
	movieid = []
	for item in result[0]['ratings']:
		tmp = {}
		movieid.append(str(item["movieid"]))
		tmp["movieid"]=item["movieid"]
		tmp["rating"]=item["rating"]
		tmp["timestamp"]=datetime.datetime.fromtimestamp(item["timestamp"]).strftime('%Y-%m-%d %H:%M:%S')
		tmp["tags"] = []
		data.append(tmp)
	sql = "select title,url,picture from movies where movieid in ({})".format(",".join(movieid))
	result_field = appbk_sql.mysql_com(sql)
	index=0
	for item in result_field:
		data[index]["title"] = item["title"]
		data[index]["url"]=item["url"]
		data[index]["picture"]= 'https://gitee.com/snaketao/douban-img/raw/master/imgg/'+str(data[index]['movieid'])+'.jpg'
		index+=1
	data = sorted(data,key=lambda x:x['timestamp'], reverse=True)
	index = 0
	res = appbk_mongo.serach_data({'movieid':{'$in':[i['movieid'] for i in data]}},'movies',{'movieid':1,'title':1,'tags':1,'_id':0})
	index = 0
	for item in res:
		while data[index]['movieid'] != item['movieid']:
			index+=1
		tagid = []
		relevance = []
		tag_name = []
		for tag in item['tags']:
			tagid.append(str(tag["tagid"]))
			relevance.append(str(tag["relevance"]))
			tag_name.append(tag["tag_name"])
		data[index]["tagid"]='\n'.join(tagid)
		data[index]["relevance"]='\n'.join(relevance)
		data[index]["tag_name"]='\n'.join(tag_name)
		index = 0
	res = {}
	res['name'] = result[0]['name']
	res['data'] = data
	return HttpResponse(json.dumps(res))

@csrf_exempt
def function_B(request):
	key_word = str(request.GET.get('key_word',''))
	sql = "SELECT movieid,title,url,picture FROM `movies` where LOWER(title)  like LOWER('%{}%');".format(key_word)
	result_field = appbk_sql.mysql_com(sql)
	res = {}
	res['data'] = result_field
	for i in res['data']:
		i['picture'] = "https://gitee.com/snaketao/douban-img/raw/master/imgg/"+str(i['movieid'])+".jpg"
	return HttpResponse(json.dumps(res))

@csrf_exempt
def function_C(request):
	type_of_movie = str(request.GET.get('type_of_movie',''))
	sql = "select movieid,movie_title , average_rating , num_of_rating,url,picture from `genres` where `genres`.genres = '{}';".format(type_of_movie)
	result_field = appbk_sql.mysql_com(sql)
	res = {}
	res['data'] = result_field
	for i in res['data']:
		i['picture'] = "https://gitee.com/snaketao/douban-img/raw/master/imgg/"+str(i['movieid'])+".jpg"
	return HttpResponse(json.dumps(res))

@csrf_exempt
def function_D(request):
	gender = str(request.GET.get('gender',''))
	sql = "SELECT movieid,title , average_rating , num_of_rating,url,picture from gender_favourite where gender = '{}';".format(gender)
	result_field = appbk_sql.mysql_com(sql)
	res = {}
	res['data'] = result_field
	for i in res['data']:
		i['picture'] = "https://gitee.com/snaketao/douban-img/raw/master/imgg/"+str(i['movieid'])+".jpg"
	return HttpResponse(json.dumps(res))

