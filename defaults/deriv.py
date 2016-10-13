from pymath import pymath_obj
from pymath.defaults.functions.seeded_func import seeded_func
from pymath.defaults.functions import default_func
class seeded_deriv(seeded_func):
	def __init__(self, dy, dx):
		super().__init__(dy, (dy, dx))
	def __str__(self):
		print(type(self[0]))

		return str(self.value) if self.known else '{}/{}'.format(*self)
class deriv(default_func):
	seeded_type = seeded_deriv
	def __init__(self, value):
		super().__init__(self, lambda x, y: x.deriv(y))
		if __debug__:
		    assert isinstance(value, pymath_obj)
		self.value = value
	
	def __truediv__(self, other):
		if not isinstance(other, deriv):
			return NotImplemented
		return self.seeded_type(self, other)
	
	def __str__(self):
		return 'd' + str(self.value.name)
	def __repr__(self):
		return '{}({})'.format(type(self).__qualname__, repr(self.value))
	@property
	def req_arg_count(self):
		return 2
