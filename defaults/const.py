from pymath import pymath_obj
class const(pymath_obj):

	def __init__(self, value = 0):
		super().__init__()
		self.value = value



	def __str__(self):
		return str(self.value)

	def __repr__(self):
		return '{}({})'.format(type(self).__qualname__, repr(self.value))

	def __eq__(self, other):
		if __debug__:
		    assert isinstance(other, pymath_obj)
		return other.known and other.value == self.value

	def deriv(self, du):
		return 0