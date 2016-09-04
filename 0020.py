# coding: utf-8
# 题目:就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。
# 思路:1.读入excel表格数据;2.对通话时间进行统计


import xlrd
import re


def get_dial_time(path):
	# 读取excel文档
	excel = xlrd.open_workbook(path)
	sheet = excel.sheet_by_name('time')

	# 统计呼出和呼进
	call_in = []
	call_out = []
	# 遍历通话记录
	for row in range(1, sheet.nrows):
		if sheet.cell(row, 4).value.encode('utf-8') == '被叫':
			call_in.append(sheet.cell(row, 3).value)
		if sheet.cell(row, 4).value.encode('utf-8') == '主叫':
			call_out.append(sheet.cell(row, 3).value)

	# 提取时间
	call_in_result = [re.findall(r'\d+', t.encode('utf-8')) for t in call_in]
	call_out_result = [re.findall(r'\d+', t.encode('utf-8')) for t in call_out]
	call_in_second = sum_time(call_in_result)
	call_out_second = sum_time(call_out_result)
	all_time = call_in_second + call_out_second
	print '%s通话被叫时长为 %s 秒, 主叫时长为 %s 秒, 通话总时长为 %s 秒, 合计 %.2f 分钟, 合计 %.2f 小时。'\
		  % (path.split('.')[0], call_in_second, call_out_second, all_time, all_time / 60.0, all_time / 3600.0)


def sum_time(result):
	second = 0
	for t in result:
		if len(t) == 1:
			second += int(t[0])
		elif len(t) == 2:
			second += int(t[0]) * 60 + int(t[1])
		else:
			second += int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2])
	return second

if __name__ == '__main__':
	get_dial_time('201604.xls')
	get_dial_time('201605.xls')
	get_dial_time('201606.xls')
