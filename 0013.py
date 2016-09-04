# coding: utf-8
# 题目:用 Python 写一个爬图片的程序，爬"http://tieba.baidu.com/p/2166231880"
# 思路:1.爬取网页;2.找到图片;3.保存图片


import urllib
from bs4 import BeautifulSoup

# 抓取网页
url = "http://tieba.baidu.com/p/2166231880"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
pictures = [s['src'] for s in soup.find_all('img', class_='BDE_Image')]
print 'There are %s pictures in url' % len(pictures)

# 保存图片
directory = '/Users/apple/PycharmProjects/python_exercise/practice/0013pictures/'
count = 1
for p in pictures:
	with open(directory + str(count) + '.jpg', 'wb') as f:
		f.write(urllib.urlopen(p).read())
	print '%s have been downloaded.' % count
	count += 1

print '%s have done!' % count
