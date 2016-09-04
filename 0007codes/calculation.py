class Rational(object):
	def __init__(self, p, q):
		self.p = p
		self.q = q

	def __add__(self, r):
		return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

	def __sub__(self, r):
		return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

	def __mul__(self, r):
		return Rational(self.p * r.p, self.q * r.q)

	def __div__(self, r):
		return Rational(self.p * r.q, self.q * r.p)

	def simplify(self):
		if self.p > self.q:
			div = self.q
			while self.p%div != 0 or self.q%div != 0:
				div = div - 1
			if self.q == div:
				return '%s' % (self.p/div)
			else:
				return '%s/%s' % (self.p/div,self.q/div)
		elif self.p < self.q:
			div = self.p
			while self.p%div != 0 or self.q%div != 0:
				div = div - 1
			return '%s/%s' % (self.p/div,self.q/div)
		else:
			return 1

	def __str__(self):
		return self.simplify()

	__repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2