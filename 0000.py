# coding: utf-8
# 题目描述:将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
# 思路:1.打开图片;2.生成字体对象;3.添加字体对象到图片;4.保存新图片
# test github
from PIL import Image, ImageFont, ImageDraw
import sys
reload(sys)

# 打开头像
image = Image.open('head.jpg', 'r')

# 建立画布
draw = ImageDraw.Draw(image)

# 确定添加字体的大小,由图片大小确定
fontsize = min(image.size)/5
# print image.size

# 添加文字
fontobj = ImageFont.truetype(font='Arial.ttf', size=fontsize)
draw.text((400, 1), '99', font=fontobj, fill=(255, 0, 0))  # RGB色块255,0,0代表红色,白色255,255,255,黑色0,0,0
image.save('head1.jpg', 'JPEG')