# coding: utf-8
# 题目描述:敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
# 思路:1.读取文档,获取敏感词集合;2.获取用户输入;3.过滤敏感词
# 提示:字符串的find函数可以返回制定子字符串的索引

# 打开敏感词文档
f = open('0011filterwords.txt', 'r')
filter_words = [w.strip() for w in f.readlines()]

# 获取用户输入
word = raw_input("Please input words(end with 'q'): ")
while word != 'q':
	for i in range(len(filter_words)):
		if word.lower().find(filter_words[i]) != -1:
			# 一旦发现有敏感词就跳出循环
			print 'Freedom.'
			break
		else:
			continue
	# 当检查完所有的敏感词后,如果还没有检测到敏感词则输出正常
	if i == len(filter_words) - 1:
		print 'Human Rights.'
	word = raw_input("Please input words(end with 'q'): ")

print 'Stop.'
