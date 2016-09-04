def new_fn(f):
	def fn(x):
		print 'call '+f.__name__+'()'
		return f(x)
	return fn

@new_fn
def f1(x):
	return x*x
@new_fn
def f2(x):
	return x*x*x
@new_fn
def f3(x):
	return x*x*x*x
print f1(9)
# print f3(9)
