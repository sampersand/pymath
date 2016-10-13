import math, numpy, pymath
class abs_vector(list, pymath.pymath_obj):
	def __init__(self: 'abs_vector', *args: (list, tuple)) -> None:
		list.__init__(self, args)
		pymath.pymath_obj.__init__(self)

	def __str__(self: 'abs_vector') -> str:
		return '<{}>'.format(', '.join(str(val) for val in self))

	def __repr__(self: 'abs_vector') -> str:
		return '{}({})'.format(type(self).__qualname__, ', '.join(repr(val) for val in self))

	def __abs__(self: 'abs_vector') -> float:
		return abs(float(self))

	def __float__(self: 'abs_vector') -> float:
		return  float(sum(val ** 2 for val in self) ** .5)

	def dot(self: 'abs_vector', other: 'abs_vector') -> pymath.pymath_obj:
		return sum(temp[0] * temp[1] for temp in zip(self, other))

	def is_perpendicular(self: 'abs_vector', other: 'abs_vector') -> bool:
		return not self.dot(other)

	def __bool__(self):
		return all(x or x is 0 or x is 0.0 for x in self)

	@classmethod
	def from_points(cls: 'abs_vector', p1: (list, tuple), p2: (list, tuple)) -> 'abs_vector':
		if __debug__:
			assert len(p1) == len(p2)
		return cls(*(temp[0] - temp[1] for temp in zip(p1, p2)))

	@property
	def freeze(self):
		return pymath.abs_vector(*[float(a) for a in self])

	@property
	def known(self):
		return all(not hasattr(e, 'known') or e.known for e in self)

	@property
	def value(self):
		if self.known:
			return pymath.point(*[float(a) for a in self])
		raise ValueError('Value not known!')

class vector(abs_vector):
	def __init__(self: 'vector', i: 'any', j: 'any', k: 'any') -> None:
		super().__init__(i, j, k)

	@property
	def i(self: 'vector') -> 'any':
		return self[0]
	
	@property
	def j(self: 'vector') -> 'any':
		return self[1]

	@property
	def k(self: 'vector') -> 'any':
		return self[2]

	# @staticmethod
	# def determinant(*args):
	#	 return numpy.linalg.det(args)
	#	 # i = a.i * (b.j * c.k - b.k * c.j)
	#	 # j = - a.j * (b.i * c.k - b.k * c.i)
	#	 # k = a.k * (b.i * c.j - b.j * c.i)
	#	 # return abs_vector(i, j, k)
	#	 # def det(a, b, c):
	#	 #	 return sum(abs_vector.determinant(a, b, c))

	def cross(self: 'vector', other: 'vector') -> 'vector':
		"""
		| i,  j,  k|
		|si, sj, sk|
		|oi, oj, ok|
		"""
		i = self.j * other.k - self.k * other.j
		j = -(self.i * other.k - self.k * other.i)
		k = self.i * other.j - self.j * other.i
		return vector(i, j, k)

	def is_parallel(self: 'vector', other: 'vector') -> bool:
		return not self.cross(other)

	def angle_between(self: 'vector', other: 'vector') -> bool:
		numer = self.dot(other)
		denom = abs(self) * abs(other)
		if abs(denom - numer) < 0.000001: #percision error fixing
			denom = numer
		return math.acos(float(numer / denom))



