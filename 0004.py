# coding: utf-8
# 题目描述:任一个英文的纯文本文件，统计其中的单词出现的个数。
# 思路:1.获取文本;2.定义split的参数sep(正则表达式);3.拆分并返回字符串,统计数量

import re
from collections import Counter

f = open('0004test.txt', 'r')
doc = f.read()
f.close()

# 英文纯文本中,分割单词的符号有
# doc1 = "I'm a boy. Sam is also a boy, but Tina is a beautiful girl.\nI read 'war and peace'"
strings = re.split(r'[\s\,\;\.\"\:]+', doc)  # [\s\,\;\.\'\"\:]+
c = Counter()
for s in strings:
	# 忽略多余字符串
	if s == '':
		continue
	else:
		c.setdefault(s, 0)
		c[s] = c[s] + 1

print sum(c.values())


# ----------------------------------------------------------------

words = re.findall(r'[a-zA-Z0-9]+', doc)
print len(words)




