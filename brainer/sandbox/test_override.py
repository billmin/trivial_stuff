import os, sys


class TEST:
	def __init__(self):
		self.a = 0.0

	def __init__(self, a):
		self.a = a

	def getA(self):
		return self.a

if __name__ == '__main__':
	t0 = TEST()
	t1 = TEST(2.0)
	print(t0.getA())
	print(t1.getA())
