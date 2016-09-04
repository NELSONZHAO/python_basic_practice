# coding: utf-8
# 题目:将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中
# 思路:1.打开并读取excel文档内容;2.写入xml文件


import xlrd
from collections import OrderedDict

comment = '''<?xml version="1.0" encoding="UTF-8"?>'''

excel = xlrd.open_workbook('0015excel.xls')
content = excel.sheet_by_name('city')

city = OrderedDict()
for row in range(3):
		city[str(row + 1)] = content.cell(row, 1).value


with open('0018city.xml', 'w') as f:
	f.write(comment + '\n')
	f.write('<root>\n')
	f.write('<cities>\n')
	f.write('<!--\n')
	f.write('\t城市信息\n')
	f.write('-->\n')
	f.write('{\n')
	for k, v in city.items():
		if k != str(len(city)):
			f.write('\t"%s" : "%s",\n' % (k.encode('utf-8'), v.encode('utf-8')))
		else:
			f.write('\t"%s" : "%s"\n' % (k.encode('utf-8'), v.encode('utf-8')))
	f.write('}\n')
	f.write('</cities>\n')
	f.write('</root>\n')

