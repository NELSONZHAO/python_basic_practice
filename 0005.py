# coding: utf-8
# 题目描述:你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# 思路:1.读取所有照片;2.循环调用分辨率调节函数;3.在函数中设置文件保存


from PIL import Image
import os

# 各手机像素
iphone6s_plus = (1920, 1080)
iphone6s = (1334, 750)
iphoneSE = (1136, 640)


def modifypx(im, size):
	# 计算缩放比例
	rate = max(im.size[0]/size[0] if im.size[0]>size[0] else 0, im.size[1]/size[1] if im.size[1]>size[1] else 0)
	if rate:
		im.thumbnail((im.size[0]/rate, im.size[1]/rate))
	new_name = im.filename.split('.')[0] + '_m.' + im.filename.split('.')[1]
	im.save(new_name, 'JPEG')


def modifypics(path='/Users/apple/PycharmProjects/python_exercise/practice/0005pics/', size=(1920,1080)):
	# 获取图片名列表
	print "There are %s pictures in current path." % str(len(os.listdir(path) - 1))
	# 读取图片并计数
	count = 1
	for pic in os.listdir(path):
		# 查看当前对象是否为图片
		if os.path.splitext(pic)[1].lower() == '.jpeg' or os.path.splitext(pic)[1].lower() =='.jpg':
			image = Image.open(path + pic, 'r')
			# 调用函数
			modifypx(image, size)
			print str(count) + ' pictures have done.'
			count += 1
		else:
			continue

if __name__ == "__main__":
	# 显示手机像素
	print '(1)iphone6s_plus: (1920, 1080)'
	print '(2)iphone6s: (1334, 750)'
	print '(3)iphoneSE: (1136, 640)\n'
	num = int(raw_input('Please select the phone pixel type:'))
	if num == 1:
		modifypics(size=iphone6s_plus)
	if num == 2:
		modifypics(size=iphone6s)
	if num == 3:
		modifypics(size=iphoneSE)
