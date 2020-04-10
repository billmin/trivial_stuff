import os, sys


class A:
	def __init__(self, a):
		self._a = a

	@property
	def a(self):
		return self._a

	def func(self, b):
		return A(self._a + b)

if __name__ == '__main__':
	a0 = A(1)
	print(a0.a)

	a1 = a0.func(2)
	print(a1.a)
