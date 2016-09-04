# coding: utf-8
# 题目: 纯文本文件 numbers.txt
# 思路:1.获取文本内容;2.创建excel表格;3.写入数据


import xlwt
import json


# 打开文件,获取数据
with open('0016numbers.txt', 'r') as f:
	numbers = json.load(f)
	# print student

# 创建工作表
wb = xlwt.Workbook()
# 创建sheet
ws = wb.add_sheet("city")

# 写入excel表格
for row in range(len(numbers)):
	for column in range(3):
		ws.write(row, column, numbers[row][column])
wb.save('0016excel.xls')
