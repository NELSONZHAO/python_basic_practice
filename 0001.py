# coding: utf-8
# 题目描述:做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# 思路:1.定义激活码格式;2.生成激活码中元素个数的数字、大小写字母;3.组成激活码


import random, string

# 生成随机数据的基本集(包括0-9,a-z,A-Z)
def createset():
	l1 = range(48, 58)  # 0-9
	l2 = range(65, 91)  # A-Z
	l3 = range(97, 123)  # a-z
	l = l1 + l2 + l3
	# l转换成ASCII码对应类型
	l_set = [chr(i) for i in l]
	# 以上代码可由 l_set = string.letters + string.digits 代替
	return l_set

# 生成4位连续码
def generate_series():
	l = createset()
	# 生成4个随机码
	s = []
	for _ in range(4):
		s.append(random.choice(l))
	return ''.join(s)
	# 以上代码可由 return ''.join(random.sample(l, 4)) 代替

# 生成16位优惠码
def generate(num):
	# 设置列表用来存储最后的优惠码
	coupons = []
	for i in range(num):
		coupon = []
		for _ in range(4):
			coupon.append(generate_series())
		coupons.append('-'.join(coupon))
	# 以上代码可由 coupons = ['-'.join([generate_series() for i in range(4)]) for i in range(num)]

	# 输出
	for c in coupons:
		print c


if __name__ == "__main__":
	num = int(raw_input("Please input the number of coupons: "))
	generate(num)
