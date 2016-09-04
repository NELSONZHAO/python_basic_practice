# coding: utf-8
# 题目:你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
# 思路:1.从当前目录读取txt文档;2.分词并统计;3.筛选出重要词汇
# collections的Counter函数可以实现

from collections import Counter
import os
import re

# 设置过滤词
stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an']


# 输出结果
def output(c, f):
	print 'The important words in %s' % f
	print 'word    frequency'
	for item in c.most_common(3):
		print item[0],  item[1]


# 计算每个文本的词
def calculate_words(path, f):
	txt = open(path + f, 'r')
	content = txt.read()
	strings = re.split(r'[\s\,\.\:\;\"\?\!]+', content)
	# 生成Counter对象,并对单词不区分大小写
	c = Counter([s.lower() for s in strings])
	# 过滤词
	for s in stop_word:
		c[s] = 0
	# 输出函数
	output(c, f)


# 导入文本
def load_files(path='/Users/apple/PycharmProjects/python_exercise/practice/0006txt/'):
	# 统计文本数量
	count = 1
	print 'There are %s files in the current path.\n' % str(len(os.listdir(path)))
	print '-' * 30
	for f in os.listdir(path):
		if os.path.splitext(f)[1].lower() == '.txt':
			calculate_words(path, f)
			print '%s txt has done.\n' % str(count)
			count += 1
		else:
			continue

if __name__ == "__main__":
	load_files()