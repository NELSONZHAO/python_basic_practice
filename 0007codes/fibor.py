class Fib(object):

    def __init__(self, num):
        self.num = num
        self.fl = []
        for i in range(self.num):
            self.fl.append(self.fibor(i))

    def fibor(self,n):
        if n <= 1:return n
        else:
            return self.fibor(n - 1) + self.fibor(n - 2)

    def __str__(self):
        return str(self.fl)

    __repr__ = __str__

    def __len__(self):
        return len(self.fl)

f = Fib(10)
print f
print len(f)