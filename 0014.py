# coding: utf-8
# 题目: 纯文本文件 student.txt为学生信息写入excel
# 思路:1.获取文本内容;2.创建excel表格;3.写入数据


import xlwt
import json


# 打开文件,获取数据
with open('0014students.txt', 'r') as f:
	student = json.load(f)
	# print student

# 创建工作表
wb = xlwt.Workbook()
# 创建sheet
ws = wb.add_sheet("student")

# 写入excel表格
for row in range(3):
	ws.write(row, 0, sorted(student.keys())[row])
	for column in range(4):
		ws.write(row, column + 1, student[str(row + 1)][column])
wb.save('0014excel.xls')



