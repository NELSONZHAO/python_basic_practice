#-*-coding:utf-8-*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from time import *
import re

#数据读取
def load_data():
	#读入电影数据
	mnames = ['movie_id','title','genres']
	movies = pd.read_csv('movies.csv',header=None,names=mnames)
	#将电影年份单独成列
	pattern = re.compile('.*?\((\d{4})\).*?')
	movies['year'] = Series([re.match(pattern,movies.ix[i]['title']).group(1) if re.match(pattern,movies.ix[i]['title']) else np.nan for i in range(len(movies))])

	#读入评分数据
	rnames = ['user_id','movie_id','rating','time']
	ratings = pd.read_csv('ratings.csv',header=None,names=rnames)

	return movies,ratings

#合并movies和ratings表以得到总表
def merge_m_r(movies,ratings):
	data_m_r = pd.merge(movies,ratings)
	#去除重复行
	data = data_m_r.drop_duplicates()
	return data

#解析时间戳并返回标准格式的字符串形式的时间
def parse_time(secs):
	return strftime("%Y-%m-%d %H:%M:%S",localtime(secs))

#查询评论数量排名在前的电影及其相应的评分,data为评分信息数据，num为选择排名前多少的电影
def rank_movie(data,num=100):
	ratings_by_title = data.groupby('title')
	#求取所有电影的平均分
	ave_rating = ratings_by_title['rating'].mean()
	#生成过滤器，过滤掉评论数据不足200条的电影，并返回Index类型数据
	active_titles = ratings_by_title.size().index[ratings_by_title.size() >= 200]
	#过滤评论数据不足1000条的电影
	ave_rating = ave_rating.ix[active_titles]
	#绘制电影评分分布图
	rank_by_ratings = ave_rating.sort_values(ascending=False)
	rank_by_ratings.plot(kind='hist',xlim=[0,5],title='Distribution of ratings',legend='ratings',bins=50,color='blue')
	#返回用户所需要的结果，并保留两位小数
	movies_num = rank_by_ratings[:num].round(2)

	return movies_num

#查询评分差异最大的电影
def diff_movie(data,num=100):
	ratings_by_title = data.groupby('title')
	#计算标准差
	rating_std_by_title = ratings_by_title['rating'].std()
	#生成过滤器，过滤掉评论数据不足200条的电影，并返回Index类型数据
	active_titles = ratings_by_title.size().index[ratings_by_title.size() >= 200]
	#根据active_titles进行过滤
	rating_std_by_title = rating_std_by_title.ix[active_titles]
	#对其进行降序排列并返回结果
	return rating_std_by_title.sort_values(ascending=False)[:num].round(2)

#查看电影每年的上映的数量
def movie_by_year(movies):
	num_by_year = movies.groupby('year').size().dropna()
	#由于2016年统计数据不完整，因此2016年数据不进行绘图
	num_by_year[:len(num_by_year)-1].plot(title='The number of movies per year')

#按照年份统计评论数量
def rating_by_year(ratings,func=parse_time):
	#解析时间后将评论年份加入ratings，方便后续处理
	ratings['time_p'] = Series([func(secs)[0:4] if secs else np.nan for secs in ratings['time']])
	num_by_year = ratings.groupby('time_p').size().dropna()
	num_by_year[:len(num_by_year)-1].plot(title='The number of ratings per year')

#统计电影的类型
def movie_genres(movies):
	#设置哑变量
	genre_iter = (set(x.split('|')) for x in movies.genres)
	genres = sorted(set.union(*genre_iter))
	dummies = DataFrame(np.zeros((len(movies),len(genres))),columns=genres)
	#迭代movies的genres列，将其对应类型的位置设置为1
	for i,gen in enumerate(movies.genres):
		dummies.ix[i,gen.split('|')] = 1
	#得到合并后的movies
	movies_windic = movies.join(dummies.add_prefix('Genres_'))
	movies_windic = movies_windic.drop('Genres_IMAX',axis=1) 
	#对每种类型的电影进行统计，绘出扇形图
	colors = ['Blue','RoyalBlue','MediumBlue','DodgerBlue','CornflowerBlue','DeepSkyBlue','SkyBlue','Azure','SlateBlue','LightBlue','PaleTurquoise','DarkCyan','DarkSlateBlue','LightSkyBlue','MediumTurquoise','Navy','SteelBlue','MidnightBlue','PowderBlue']
	movies_windic.ix[:,5:].sum().plot(kind='pie',title='The Pie of Genres',colors=colors)
	return movies_windic

#计算每种类型电影的评分及评论数量
def rating_by_genres(movies_windic,ratings):
	#合并数据并去除重复值
	data = pd.merge(movies_windic,ratings).drop_duplicates()
	#计算每种电影的评分和数量，存入字典中
	genre_ratings = {}
	genre_num = {}
	for genre in movies_windic.columns[5:]:
		#将每种电影的评分存入字典
		genre_ratings[genre] = data.groupby(genre)['rating'].mean()[1]
		#将每种电影的评论总数量存入字典
		genre_num[genre] = data.groupby(genre).size()[1]
	#返回Series对象，方便绘图
	s_ratings = Series(genre_ratings)
	s_num = Series(genre_num)
	#为了消除电影数量给评论数量造成的差异，在这里对每种类型的电影做标准处理，用评论总数量/电影总数量
	p_num = Series(movies_windic.ix[:,5:].sum())
	s_p_num = s_num/p_num
	return s_ratings, s_p_num

#计算每种电影上映数量随着年的变化
def genre_by_years(movies_windic):
	#设置一个字典用来存储每种类型电影的时间序列变化
	genre_dict = {}
	for genre in movies_windic.columns[5:]:
		genre_dict[genre.lower()] = pd.crosstab(movies_windic.year,movies_windic[genre])[1]
	#将字典转换为dataframe格式
	genre_df = DataFrame(genre_dict)
	#设置绘图颜色
	colors = ['Pink','DeepPink','Violet','MediumPurple','GhostWhite','Blue','SlateGray','SkyBlue','LightGreen','GreenYellow','Cornsilk','DarkOrange','Tan','Cyan','Red','Sienna','Navy','Thistle']
	genre_df.ix[:len(genre_df)-1].plot(title='The number of ratings per year by genres',colors=colors)

"""#计算每种类型电影的评分随着年的变化
def genre_rating_by_year(movies_windic,ratings,func=parse_time):
	#设置一个字典用来存储每种类型电影评分的时间序列变化
	genre_dict = {}
	result = {}
	
	#解析评论时间
	ratings['time_p'] = Series([func(secs)[0:4] if secs else np.nan for secs in ratings['time']])
	data = pd.merge(movies_windic,ratings).drop_duplicates()
	#循环合并表，取出每种类型电影的信息
	for genre in movies_windic.columns[5:]:
		genre_dict[genre] = data[data[genre]==1].ix[:,[genre,'rating','time_p']]
	#开始计算每种类型电影的评分时间序列
	for genre in movies_windic.columns[5:]:
		result[genre] = genre_dict[genre].groupby('time_p')['rating'].mean()
	#将字典转换成为dataframe格式
	rating_df = DataFrame(result)
	return rating_df"""

#计算每种类型电影评分较前的电影
def movie_by_genres(movies_windic,ratings):
	#设置字典存储每种类型电影的信息
	genre_dict = {}
	#设置字典存储最后每种类型电影的评分较前的电影
	result = {}
	#合并两个表
	data = pd.merge(movies_windic,ratings).drop_duplicates()
	#循环遍历整个data表，取出每种类型电影的信息
	for genre in movies_windic.columns[5:]:
		genre_dict[genre] = data[data[genre]==1].ix[:,['title','rating']]
	#循环每种类型电影的字典，对title进行groupby，并且设定评论数量的筛选条件
	for genre in movies_windic.columns[5:]:
		#每次循环前清空上一次循环的变量
		ratings_by_title = ''
		active_titles = ''
		ave_rating = ''
		#先筛选出每种类型电影中评论数量大于等于200的电影
		ratings_by_title = genre_dict[genre].groupby('title')
		active_titles = ratings_by_title.size().index[ratings_by_title.size() >= 200]
		ave_rating = ratings_by_title.mean().ix[active_titles]
		result[genre] = ave_rating.sort_values(by='rating',ascending=False)[:20]
	return result

#选择哪一种类型的电影排名
def select_genres(movies_windic,result):
	#定义类型list
	genres = []
	i = 1
	#将类型存储并且打印出来供用户选择
	for genre in movies_windic.columns[5:]:
		genres.append(genre)
		print str(i) + ':' + str(genre)
		i += 1

	#接受用户选择
	num = int(raw_input('请输入您所想选择的类型编号：'))
	output = result[genres[num-1]]
	print "您所选择的类型是：" + str(genres[num-1])
	print output.round(2)
