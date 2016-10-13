import pymath
from pymath import pymath_container, pymath_obj
from pymath.defaults import const
class seeded_func(pymath_container):
	@staticmethod
	def scrub(args):
		return tuple(x if isinstance(x, pymath_obj) else const(x) for x in args)

	def __init__(self, func_instance, args_to_pass_to_func):
		super().__init__(self.scrub(args_to_pass_to_func))
		self.func_instance = func_instance

	def __str__(self) -> str:
		return str(self.value) if self.known else self.func_instance._def_str(self._iterable)

	@property
	def value(self):
		return self.func_instance.inp_func(*self)

	def __repr__(self):
		return '{}({}, {})'.format(type(self).__qualname__, repr(self.func_instance), repr(self._iterable))


class seeded_oper(seeded_func):
	def __new__(cls, func_instance, args_to_pass_to_func):
		args_to_pass_to_func = cls.scrub(args_to_pass_to_func)
		identity = func_instance._is_identity(*args_to_pass_to_func)
		if identity is not None and 0:
			return identity
		else:
			return seeded_func.__new__(cls)
	def __init__(self, func_instance, args_to_pass_to_func):
		super().__init__(func_instance, args_to_pass_to_func)
		if __debug__:
		    assert isinstance(func_instance, pymath.defaults.functions.oper.oper)

	def deriv(self, du):
		name = self.func_instance.name
		a = self[0]
		b = self[1]
		if name == '+': return a.deriv(du) + b.deriv(du)
		if name == '-': return a.deriv(du) - b.deriv(du)
		if name == '*':
			if isinstance(a, const):
				return a * b.deriv(du)
			if isinstance(b, const):
				return a.deriv(du) * b
			return a.deriv(du) * b + a * b.deriv(du)
		if name == '/':
			pass
		if name == '**':
			# print(a, b)
			power = b
			base = a
			print(base.deriv(du), base, sep = '|')
			if base.deriv(du) and not power.deriv(du):
				# power1 = power - 1
				# comb = base ** power1
				# comb2 = power * comb
				# print(repr(comb2))
				# print(repr(comb2[0]))
				# print(comb2[0])
				# # print(comb2 * 1 )
				# quit()
				return power * base ** (power - 1) * base.deriv(du)
			# if isinstance(a, pymath_obj) and not isinstance(b, pymath_obj):
			# if isinstance(b, pymath_obj) and not isinstance(a, pymath_obj):
			# 	return (a ** b) * pymath.math.ln(a) * b.deriv(du)

		raise ValueError('No way to take the derivative of  \'' + str(name) + '\'')

	def __str__(self) -> str:
		return self.func_instance._def_str(self._iterable)














