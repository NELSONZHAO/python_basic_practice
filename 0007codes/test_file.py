class Student(object):
	def __init__(self, name):
		self.name = name
		# self.score = score

def compare(x,y):
	if x>y: return -1
	elif x<y: return 1
	else: return 0
L = [Student('Adam'), Student('Lisa'), Student('Bart')]
L1 = sorted(L, compare)
for _ in L1:
	print _.name
