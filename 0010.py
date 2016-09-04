# coding: utf-8
# 题目:使用 Python 生成类似于下图中的字母验证码图片
# 思路:1.创建画布;2.导入字母库,写入字母;3.保存图片


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string
import random

# 定义大小
width = 60 * 4
height = 60
# 创建一个图片
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建font对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=(random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)))
# 获取文字
chs = random.sample(string.letters, 4)
# 输出文字
for t in range(4):
	draw.text((60 * t, 10), chs[t].upper(), font=font, fill=(random.randint(37, 127), random.randint(37, 127), random.randint(37, 127)))

# 模糊图片
image = image.filter(ImageFilter.BLUR)
image.save('0010code.jpg', 'JPEG')