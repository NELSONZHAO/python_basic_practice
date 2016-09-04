# coding: utf-8

import urllib
from bs4 import BeautifulSoup
import re
import pymysql

resp = urllib.urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode('utf-8')
soup = BeautifulSoup(resp, "html.parser", from_encoding="utf8")

result = soup.find_all("a", href=re.compile(r'^/wiki/'))
for url in result:
	if not re.search("\.(jpg|JPG)$", url["href"]):
		print url.get_text(),"<---->", "https://en.wikipedia.org"+url["href"]
		conn = pymysql.connect(host="localhost",user="root",password="940720",db="imooc",charset="utf8mb4")
		try:
			with conn.cursor() as cursor:
				sql = "INSERT INTO wikiurl(urlname,urlhref) values(%s,%s)"
				cursor.execute(sql,(url.get_text(),"https://en.wikipedia.org"+url["href"]))
				conn.commit()
		finally:
			cursor.close()
			conn.close()