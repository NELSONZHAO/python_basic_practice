# coding: utf-8
# 题目:将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中
# 思路:1.打开并读取excel文档内容;2.写入xml文件


import xlrd
from collections import OrderedDict

comment = '''<?xml version="1.0" encoding="UTF-8"?>'''
desc = '''"id" : [名字, 数学, 语文, 英文]'''

excel = xlrd.open_workbook('0014excel.xls')
content = excel.sheet_by_name('student')

student = OrderedDict()
for row in range(3):
	student.setdefault(str(row + 1), [])
	for column in range(4):
		student[str(row + 1)].append(content.cell(row, column + 1).value)

# print student

with open('0017xml.xml', 'w') as f:
	f.write(comment + '\n')
	f.write('<root>\n')
	f.write('<students>\n')
	f.write('<!--\n')
	f.write('\t学生信息表\n')
	f.write('\t' + desc + '\n')
	f.write('-->\n')
	f.write('{\n')
	for k, v in student.items():
		if k != str(len(student)):
			f.write('\t"%s" : ["%s", %d, %d, %d],\n' % (k.encode('utf-8'), v[0].encode('utf-8'), v[1], v[2], v[3]))
		else:
			f.write('\t"%s" : ["%s", %d, %d, %d]\n' % (k.encode('utf-8'), v[0].encode('utf-8'), v[1], v[2], v[3]))
	f.write('}\n')
	f.write('</students>\n')
	f.write('</root>\n')

