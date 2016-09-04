# coding: utf-8
# 题目:一个HTML文件，找出里面的正文。
# 思路:1.读取文档;2.解析文档;3.提取正文


from bs4 import BeautifulSoup
import urllib
import re


def parse_html(html):
	soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
	for s in soup.find_all('p'):
		print s.get_text().strip()

# 正则表达式方法
def get_body(url):
	html_content = urllib.urlopen(url).read()
	r = re.compile('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
	result = r.findall(html_content)
	return result


if __name__ == "__main__":
	url = raw_input("Please input url: ")
	doc = urllib.urlopen(url).read()
	parse_html(doc)
