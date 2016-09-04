#-*-coding:utf-8 -*-
import urllib2
import shutil

#读取队伍编号
f = open('/Users/apple/allmcmpdf/mcmnum.txt','r')
lines = f.readlines()
nums = []
for line in lines:
	nums.append(line.strip('\n'))

#从nums中读取编号
for num in nums:
	try:
		url = 'http://www.comap-math.com/mcm/2016Certs/' + str(num) + '.pdf'
		req = urllib2.urlopen(url)
		with open('/Users/apple/allmcmpdf/' + str(num) + '.pdf', 'w') as fp:
			shutil.copyfileobj(req, fp)
		print '已下载' + str(num) + '队伍的获奖证书'
	except urllib2.URLError, e:
		if hasattr(e, "code"):
			print str(e.code) + '这个组可能没成绩！'
		continue