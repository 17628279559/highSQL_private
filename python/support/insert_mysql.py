#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 snaketao. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2021-12-12 17:26
# @FileName: insert_mysql.py
# @Desc    : insert data to mysql
import appbk_sql
import numpy as np

#计算每个movieid的平均评分并插入到mysql
def function_insert_average_rating():  #insert_average_rating_to_mysql
    sql = "SELECT movieid,AVG(rating) average_rating,count(*) num_of_rating from ratings GROUP BY movieid;"
    result = appbk_sql.mysql_com(sql)
    appbk_sql.insert_data_list(result, 'average_rating')

#将每个风格最推荐的20个电影插入mysql
def function_C_support():
	genres = ['Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy', 'Romance', 'Drama', 'Action', 'Crime', 'Thriller', 'Horror', 'Mystery', 'Sci-Fi', 'IMAX', 'Documentary', 'War', 'Musical', 'Western', 'Film-Noir']
	for genre in genres:
		sql = "select title,average_rating,num_of_rating from movies a,average_rating b WHERE a.movieid = b.movieid and a.movieid in (select movieid from movies where genres LIKE '%{}%');".format(genre)
		result_field = appbk_sql.mysql_com(sql)
		movies = []
		for item in result_field:
			movies.append([item["title"],item["average_rating"],item["num_of_rating"]])
		movies = sorted(movies, key = lambda x:float(x[1])*np.log(np.log(float(x[2]+1))),reverse = True)[:20]
		for i in movies:
			sett = {'genres':genre , 'movie_title':i[0],'average_rating':i[1],"num_of_rating":i[2]}
			#appbk_sql.insert_data(sett,'genres')
		print(genre)

#将男女性别最推荐的20个电影插入mysql
def function_D_support():
	genders = ["Man","Female"]
	movies = {}
	movies["Man"] = []
	movies["Female"] = []
	for gender in genders:
		sql = "SELECT movieid,title, avg( rating ) average_rating, count(rating) num_of_ratng FROM (SELECT a.movieid,a.rating,b.title from ratings a,movies b where `userid` in (SELECT userid from users where gender = '{}') and a.movieid = b.movieid) c GROUP BY movieid ;".format(gender)
		result_field = appbk_sql.mysql_com(sql)
		for item in result_field:
			movies[gender].append([item["movieid"],item["title"],item["average_rating"],item["num_of_ratng"]])
		movies[gender] = sorted(movies[gender], key = lambda x:float(x[2])*np.log(float(x[3]+2)),reverse = True)[:20]
		for item in movies[gender]:
			sett = {'gender':gender , 'movieid':item[0],'title':item[1],"average_rating":item[2],"num_of_rating":item[3]}
			appbk_sql.insert_data(sett,'gender_favourite')
			print(item)

if __name__=="__main__":
    #function_insert_average_rating()
	#function_C_support()
	#function_D_support()
	pass