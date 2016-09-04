# coding: utf-8
# 题目:通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
# 思路:1.获取用户密码;2.加密;3.返回加密结果

import hashlib
import hmac
import random


def encrypt(password, salt=None):
	if salt == None:
		salt = hashlib.sha256(str(random.random())).hexdigest()[-8:]
	# 如果密码是unicode格式需要转换成utf-8
	if isinstance(password, unicode):
		password = password.encode('utf-8')
	psw = hmac.HMAC(salt, password, hashlib.sha256).hexdigest()
	return '%s$%s' % (salt, psw)

def validate(input, psw):
	salt = psw.split('$')[0]
	return psw == encrypt(input, salt)


if __name__ == "__main__":
	password_input1 = raw_input('Password: ')
	password_input2 = raw_input('Password: ')
	salt = '19940720'
	en_psw1 = encrypt(password_input1)
	en_psw2 = encrypt(password_input2)
	print en_psw1
	print en_psw2
	print validate(password_input1, en_psw1)
	print validate(password_input2, en_psw1)
