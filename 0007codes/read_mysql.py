# coding: utf-8

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='940720',db='imooc',charset='utf8mb4')
try:
	with conn.cursor() as cursor:
		sql = "SELECT urlname,urlhref FROM wikiurl WHERE id IS NOT NULL"
		rcount = cursor.execute(sql)
		print cursor.rowcount
		print rcount

		rs1 = cursor.fetchone()
		rs2 = cursor.fetchmany(3)
		rs3 = cursor.fetchall()
		print rs1
		print rs2
		print rs3
finally:
	cursor.close()
	conn.close()