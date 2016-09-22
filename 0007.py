# coding: utf-8
# 题目:有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
# 思路:1.遍历目录,导入文件;2.统计代码、空行、注释的数量;3.输出/并统计所有代码、空行、注释数量(与代码在同一行的注释忽略不计)


import os
import re

# 代码文件尾缀
postfix = ['.c', '.py', '.html', '.htm', '.asp', '.jsp', '.php']

#总的统计字典
result = {'fnum': 0, 'codes': 0, 'blanks': 0, 'notes': 0, 'alls': 0}


# 统计数量
def calculate_codes(path, f):
	codes = open(path + f, 'r')
	# 定义一个列表存储当前代码的每一行
	tlines = []
	# 循环遍历当前文件的每一行
	for line in codes.readlines():
		tlines.append(line)
	# 对结果行进行去除空格、制表符以及换行符
	result = [t.strip() for t in tlines]

	# 开始统计数量
	total = {'fname': f, 'code': 0, 'blank': 0, 'note': 0, 'all': len(result)}
	for line in result:
		if line == '':
			total['blank'] += 1
		elif re.match(r'#', line):
			total['note'] += 1
		else:
			total['code'] += 1

	for k, v in total.items():
		print k, v

	return total


# 总输出
def total_add(calc_result):
	result['fnum'] += 1
	result['codes'] += calc_result['code']
	result['blanks'] += calc_result['blank']
	result['notes'] += calc_result['note']
	result['alls'] += calc_result['all']


# 加载文件
def load_file(path='/Users/apple/Desktop/python_files/'):
	# 输出文件数量
	print "There are %s code files in current path." % len(os.listdir(path))
	print '-' * 30
	for cf in os.listdir(path):
		# 判断是否为代码文件
		if os.path.splitext(cf)[1] in postfix:
			code_total = calculate_codes(path, cf)
			# 将每个文件的统计结果传递给总统计函数
			total_add(code_total)
			print '-' * 30
		else:
			continue


if __name__ == "__main__":
	load_file()
	for k, v in result.items():
		print k, v
