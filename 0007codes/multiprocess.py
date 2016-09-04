# coding: utf-8

import os, time, random
from multiprocessing import Process
import Queue

# 写数据进程执行的代码


def write(q):
	for value in ['A','B','C']:
		print 'Put %s to queue...' % value
		q.put(value)
		time.sleep(random.random())

# 读数据进程执行的代码


def read(q):
	while True:
		if not q.empty():
			value = q.get(True)
			print 'Get %s from queue.' % value
			time.sleep(random.random())
		else:
			break

if __name__ == "__main__":
	q = Queue.Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	# 启动子进程写入
	pw.start()
	# 等待pw结束
	pw.join()
	# 启动子进程读取
	pr.start()
	pr.join()

	print
	print '所有数据都写入并且读完'