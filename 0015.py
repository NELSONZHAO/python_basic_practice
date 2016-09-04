# coding: utf-8
# 题目: 纯文本文件 city.txt为城市信息
# 思路:1.获取文本内容;2.创建excel表格;3.写入数据


import xlwt
import json


# 打开文件,获取数据
with open('0015city.txt', 'r') as f:
	city = json.load(f)
	# print student

# 创建工作表
wb = xlwt.Workbook()
# 创建sheet
ws = wb.add_sheet("city")

# 写入excel表格
for row in range(len(city)):
	ws.write(row, 0, sorted(city.keys())[row])
	for column in range(1):
		ws.write(row, column + 1, city[str(row + 1)])
wb.save('0015excel.xls')
