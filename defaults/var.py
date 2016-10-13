import re, inspect
from pymath import pymath_obj
class var(pymath_obj):
	lambda_regex = re.compile(r'(?P<name>\w+)\s*=\s*(?P<value>.+)$')

	def __init__(self, name = None, value = None):
		super().__init__(name, value)
	
	def __str__(self):
		if self.known:
			# if self.hasname:
			# 	return str(self.value)
				# return '{{{}:{}}}'.format(self.name, self.value)
			return str(self.value)
		return str(self.name)

	def __repr__(self: 'var') -> str:
		return '{}({}, {})'.format(type(self).__qualname__, self.name, self.value)

	def __call__(self, to_mul_against):
		return self * to_mul_against

	# def __eq__(self, other):
	# 	if __debug__:
	# 	    assert isinstance(other, pymath_obj)
	# 	if self.name == other.name:
	# 		if __debug__:
	# 			assert self.known == other.known
	# 			assert not self.self or self.value == other.value
	# 		return True
	# 	return self.known and other.known and self.value == other.value

	def deriv(self, du):
		return 0 if self.known or self != du else 1









