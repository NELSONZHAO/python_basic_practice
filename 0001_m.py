# coding: utf-8
# 题目描述:做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# 思路:1.定义激活码格式;2.生成激活码中元素个数的数字、大小写字母;3.组成激活码


import random, string

# 生成随机数据的基本集(包括0-9,a-z,A-Z)
def createset():
	l_set = string.letters + string.digits
	return l_set

# 生成4位连续码
def generate_series():
	return ''.join(random.sample(createset(), 4))

# 生成16位优惠码
def generate(num):
	coupons = ['-'.join([generate_series() for _ in range(4)]) for _ in range(num)]

	# 输出
	for c in coupons:
		print c


if __name__ == "__main__":
	num = int(raw_input("Please input the number of coupons: "))
	generate(num)
