# coding: utf-8
# 题目:一个HTML文件，找出里面的链接。
# 思路:1.加载网页信息;2.解析信息;3.提取链接

import urllib
from bs4 import BeautifulSoup
import urlparse

url = raw_input("Please input your url: ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
urls = []
for s in soup.find_all('a'):
	if s.has_attr('href'):
		urls.append(s['href'])
	else:
		continue
# 将以'/'开头的残缺url补全
for u in urls:
	if u[0] == '/':
		print 'http://' + urlparse.urlsplit(url).netloc + u
	else:
		print u