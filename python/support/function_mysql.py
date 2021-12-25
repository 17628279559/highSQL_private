#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 snaketao. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2021-12-10 22:53
# @FileName: function_mysql.py
# @Desc    : query function by mysql
import appbk_sql
import sys
import numpy as np

#查询id对应的人看过的所有电影，并且输出每个电影最相关的前三个标签
def function_A(id,ban_movieid = []):
	sql1 = "SELECT `name` FROM `users` WHERE `userid` = {}".format(str(id))
	name = appbk_sql.mysql_com(sql1)[0]['name']
	sql2 = "SELECT	b.movieid, b.title, a.rating FROM `ratings` as a, `movies` as b WHERE a.movieid = b.movieid  AND a.userid = {};".format(str(id))
	result_field = appbk_sql.mysql_com(sql2)  #获取movieid 对应 title 和 对应rating

	movies = {}
	movies["name"] = name
	movieids = []
	num = 0
	for item in result_field:
		if item['movieid'] not in ban_movieid:
			movies[str(item['movieid'])] = {}
			movieids.append(str(item['movieid']))
			movies[str(item['movieid'])]["title"] = item['title']
			movies[str(item['movieid'])]["rating"] = item['rating']
			movies[str(item['movieid'])]["tag"] = []
		num+=1
		if num == 20:
			break


	sql3 = "SELECT a.movieid,a.relevance, b.tag FROM `genome-scores` a , `genome-tags` b WHERE a.tagid = b.tagid AND movieid IN ({}) ORDER BY a.movieid,a.relevance DESC;".format(','.join(movieids))
	result_field1 = appbk_sql.mysql_com(sql3)
	i = 0
	while i<len(result_field1):
		movies[str(result_field1[i]['movieid'])]["tag"].append([result_field1[i]['tag'],result_field1[i]['relevance']])
		if i%1128 == 2:
			i+=1126
		else:
			i+=1
	#print(movies["name"],'看过的电影有:')
	#for item in movies:
	#	if item != "name":
	#		print('%-50s'%movies[item]["title"],'    评分为:','%-10s'%str(movies[item]["rating"]) ,end="")
	#		print("    相关标签:",end = "")
	#		for tag in movies[item]["tag"]:
	#			print('%-40s'%(str(tag[0])+'-->相关度:'+str(tag[1])[:7]),end="    ")
	#		print("\n")
	movies["ban_movieid"] = ban_movieid.append(movieids)
	return movies

#查询含有关键字的电影
def function_B(key_word):
	sql = "SELECT title FROM `movies` where LOWER(title)  like LOWER('%{}%');".format(key_word)
	result_field = appbk_sql.mysql_com(sql)
	for item in result_field:
		print(item)
	return result_field

#查询不同风格类型的最受欢迎的20部电影
def function_C(type_of_movie):
	sql = "select movie_title , average_rating , num_of_rating from `genres` where `genres`.genres = '{}';".format(type_of_movie)
	result_field = appbk_sql.mysql_com(sql)
	#for item in result_field:
	#	print(item)
	return result_field

#查询不同性别最受欢迎的20部电影
def function_D(gender):
	sql = "SELECT title , average_rating , num_of_rating from gender_favourite where gender = '{}';".format(gender)
	result_field = appbk_sql.mysql_com(sql)
	for item in result_field:
		print(item)
	return result_field

if __name__=="__main__":
	#function_A(21)
	#function_B("girls")
	#function_C("Animation")
	#function_D("Man")
	pass