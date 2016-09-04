# coding: utf-8
# 题目:将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中
# 思路:1.打开并读取excel文档内容;2.写入xml文件


import xlrd
from collections import OrderedDict

comment = '''<?xml version="1.0" encoding="UTF-8"?>'''

excel = xlrd.open_workbook('0016excel.xls')
content = excel.sheet_by_name('numbers')

numbers = OrderedDict()
for row in range(3):
	numbers.setdefault(str(row), [])
	for column in range(3):
		numbers[str(row)].append(content.cell(row, column).value)

# print student

with open('0019xml.xml', 'w') as f:
	f.write(comment + '\n')
	f.write('<root>\n')
	f.write('<numbers>\n')
	f.write('<!--\n')
	f.write('\t数字信息\n\n')
	f.write('-->\n')
	f.write('[\n')
	for k, v in numbers.items():
		if k != str(len(numbers)-1):
			f.write('\t[%d, %d, %d],\n' % (v[0], v[1], v[2]))
		else:
			f.write('\t[%d, %d, %d]\n' % (v[0], v[1], v[2]))
	f.write(']\n')
	f.write('</numbers>\n')
	f.write('</root>\n')

