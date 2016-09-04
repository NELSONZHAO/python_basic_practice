# coding: utf-8
# 题目描述:敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
# 思路:1.读取文档,获取敏感词集合;2.获取用户输入;3.过滤敏感词并替换


# 打开敏感词文档
f = open('0011filterwords.txt', 'r')
filter_words = [w.strip() for w in f.readlines()]

# 获取用户输入
word = raw_input("Please input words(end with 'q'): ")
while word != 'q':
	for i in range(len(filter_words)):
		if word.find(filter_words[i]) != -1:
			# 一旦发现有敏感词就替换敏感词
			word = word.replace(filter_words[i], '**')
		else:
			continue
	# 当检查完所有的敏感词后,输出结果
	print word
	word = raw_input("Please input words(end with 'q'): ")

print 'Stop.'
