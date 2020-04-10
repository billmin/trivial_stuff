import os, sys
import random


class Point:
	def __init__(self, symbol_name, dim=2, pt=None):
		self._symbol_name = symbol_name
		if pt is None:
			p = []
			for i in range(dim):
				p.append(random.random())
			##
			self._dim = dim
			self._point = tuple(p)
		else:
			try:
				if dim != len(pt):
					raise ValueError("ValueError: class Point: in __init__ 'dim' conficts with given 'pt'")

				if not isinstance(pt, (tuple, list)):
					raise TypeError("TypeError: class Point: in __init__ type error of 'pt'")
				
				self._dim = dim
				self._point = pt if isinstance(pt, tuple) else tuple(pt)
			except Exception as err:
				print(err)

	@property
	def symbol_name(self):
		return self._symbol_name

	@property
	def dim(self):
		return self._dim

	@property
	def point(self):
		return self._point

	def moveto(self, bias):
		if len(bias) == self._dim and isinstance(bias, (tuple, list)):
			p = []
			for i in range(self._dim):
				p.append(self._point[i]+bias[i])
			self._point = tuple(p)

	def isIdentityOf(self, pt):
		if self._dim == pt.dim:
			for i in range(self._dim):
				if self._point[i] != pt.point[i]:
					return False
			return True
		else:
			return False

# for test
class Dummy:
	def __init__(self, v):
		self._v = v
	
	@property
	def v(self):
		return self._v


if __name__ == '__main__':
	p0 = Point('p0', 3)
	p1 = Point('p1', 3, (1.0, 2.0, 3.0))
	p2 = Point('p2', 3, (10.0, 10.0, 10.0))
	bias = (0, 3.0, 1.0)

	print('p0: ', p0.point)
	print('p0 isIdentityOf p1: ', p0.isIdentityOf(p1))
	print('before moving by bias: ', bias)
	print('p2: ', p2.point)
	p2.moveto(bias)
	print('after moving by bias: ', bias)
	print('p2: ', p2.point)

