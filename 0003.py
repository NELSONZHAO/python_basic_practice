# coding: utf-8
# 题目描述:把激活码存入Redis非关系型数据库
# 思路:1.定义激活码格式;2.生成激活码中元素个数的数字、大小写字母;3.组成激活码;4.存储激活码


import random, string, redis

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
	return coupons

# 存储到数据库
def saveredis(coupons):
	r = redis.Redis('localhost', 6379)
	for c in coupons:
		r.sadd("code", c)
	r.save()


if __name__ == "__main__":
	num = int(raw_input("Please input the number of coupons: "))
	result = generate(num)
	# 是否写入数据库
	print "Would you like to save these coupons into database?(y/n)"
	select = raw_input()
	if select.lower() == 'y':
		saveredis(result)
	else:
		print "Done."
