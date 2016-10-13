import re, inspect
from pymath import pymath_obj
from pymath.defaults import const
from pymath.defaults.functions import default_func
from pymath.defaults.functions.seeded_func import seeded_oper
oper_priorities = {}
class oper(default_func):
	seeded_type = seeded_oper
	def __init__(self, name, inp_func, identity_func, is_r = False):
		super().__init__(inp_func, name)
		self.is_r = is_r
		self._is_identity = identity_func


	def _binary_oper_str(self, a, b):
		# assert 
		if self.name == '*':
			if hasattr(a, 'known') and a.known:
				if __debug__:
					assert not b.known #if they are both known, it should be str(value)
				return str(a) + self._add_parens_if_lower_oper(b)
			elif hasattr(b, 'known') and b.known:
				if __debug__:
					assert not a.known #if they are both known, it should be str(value)
				return str(b) + self._add_parens_if_lower_oper(a)

		return '{0}{1}{2}{1}{3}'.format(self._add_parens_if_lower_oper(a), self.name in {'+', '-'} and ' ' or '',
		                                self.name, self._add_parens_if_lower_oper(b))

	def _add_parens_if_lower_oper(self, arg):
		if not isinstance(arg, seeded_oper):
			return str(arg)
		if not arg.known and oper_priorities[arg.func_instance] > oper_priorities[self]:
			return '(' + str(arg) + ')'
		return str(arg)

	def _def_str(self, print_args):
		if __debug__:
			assert len(print_args) == self.req_arg_count #required.
		if self.req_arg_count == 1:
			return '{}{}'.format(self.name, self._add_parens_if_lower_oper(print_args[0]))
		elif self.req_arg_count == 2:
			if self.is_r:
				return self._binary_oper_str(print_args[1], print_args[0])
			return self._binary_oper_str(print_args[0], print_args[1])
		else:
			raise ValueError('uh oh!')
	def __hash__(self):
		return hash(str(self) + str(self.inp_func))
	# def __str__(self):
	# 	return super().super().__str__()
def known_coerce(arg, *values):
	return arg.known and arg.value in values
opers = {
	'__add__': oper('+',
	                inp_func = lambda l, r: l.value + r.value,
	                identity_func = lambda l, r: 
	                	 +r if known_coerce(l, 0) else
	                	 (l if known_coerce(r, 0) else None)),
	'__sub__': oper('-',
	                inp_func = lambda l, r: l.value - r.value,
	                identity_func = lambda l, r: 
	                	-r if known_coerce(l, 0) else
	                	(l if known_coerce(r, 0) else None)
	               	),
	'__mul__': oper('*',
	                inp_func = lambda l, r: l.value * r.value,
	                identity_func = lambda l, r: 
	                	 0 if known_coerce(l, 0) or known_coerce(r, 0) else
	                	(r if known_coerce(l, 1) else
	                	(l if known_coerce(r, 1) else
	                	None))
	               	),
	'__truediv__': oper('/',
	                inp_func = lambda n, d: n.value / d.value,
	                identity_func = lambda n, d: 
	                	 n if known_coerce(d, 1) else
	                	(1 if n == d or n.known and known_coerce(d, n.value) else None)
	               	),
	'__floordiv__': oper('//',
	                inp_func = lambda n, d: n.value // d.value,
	                identity_func = lambda n, d: 
	                	n if known_coerce(d, 1) else None
	               	),
	'__pow__': oper('**',
	                inp_func = lambda b, p: b.value ** p.value,
	                identity_func = lambda b, p: 
	                	b if known_coerce(p, 1) else
	                	(1 if known_coerce(p, 0) else
	                	(b if known_coerce(b, 1, 0) else
	                	  None))
	               	),
	'__mod__': oper('%',
	                inp_func = lambda dd, dv: dd.value ** dv.value,
	                identity_func = lambda dd, dv: 
	                	0 if known_coerce(dv, 1) else None
	               	),
# 	'__lt__': oper('<', lambda a, b: coerce(a) < b.value),
# 	'__gt__': oper('>', lambda a, b: coerce(a) > b.value),
# 	'__eq__': oper('==', lambda a, b: coerce(a) == b.value),
# 	'__ne__': oper('!=', lambda a, b: coerce(a) != b.value),
# 	'__ge__': oper('>=', lambda a, b: coerce(a) >= b.value),
# 	'__le__': oper('<=', lambda a, b: coerce(a) <= b.value),
	'__radd__': oper('+',
	                inp_func = lambda r, l: l.value + r.value,
	                identity_func = lambda r, l: 
	                	+r if known_coerce(l, 0) else
	                	 (l if known_coerce(r, 0) else None),
	                	 is_r = True),
	'__rsub__': oper('-',
	                inp_func = lambda r, l: l.value - r.value,
	                identity_func = lambda r, l: 
	                	-r if known_coerce(l, 0) else
	                	(l if known_coerce(r, 0) else None)
	               	,
	               	is_r = True),
	'__rmul__': oper('*',
	                inp_func = lambda r, l: l.value * r.value,
	                identity_func = lambda r, l:
	                	0 if known_coerce(l, 0) or known_coerce(r, 0) else
	                	(
	                	 # print(r, known_coerce(l, 1))
	                	   +r if known_coerce(l, 1) else
	                	  (l if known_coerce(r, 1) else None)
	                	)
	               	,
	               	is_r = True),
	'__rtruediv__': oper('/',
	                inp_func = lambda d, n: n.value / d.value,
	                identity_func = lambda d, n: 
	                	 n if known_coerce(d, 1) else
	                	(1 if n == d or n.known and known_coerce(d, n.value) else None)
	               	,
	               	is_r = True),
	'__rfloordiv__': oper('//',
	                inp_func = lambda d, n: n.value // d.value,
	                identity_func = lambda d, n: 
	                	n if known_coerce(d, 1) else None
	               	,
	               	is_r = True),
	'__rpow__': oper('**',
	                inp_func = lambda p, b: b.value ** p.value,
	                identity_func = lambda p, b: 
	                	b if known_coerce(p, 1) else
	                	(1 if known_coerce(p, 0) else
	                	((b if known_coerce(b, 1, 0) else
	                	  None)))
	               	,
	               	is_r = True),
	'__rmod__': oper('%',
	                inp_func = lambda dv, dd: dd.known ** dv.known,
	                identity_func = lambda dv, dd: 
	                	0 if known_coerce(dv, 1) else None
	               	),

	'__invert__': oper('~',
	                inp_func = lambda a: ~_coerce(a),
	                identity_func = lambda a: None
					),

	'__neg__': oper('-',
	                inp_func = lambda a: -_coerce(a),
	                identity_func = lambda a: 0 if known_coerce(a, 0) else None
					),
	'__pos__': oper('+',
	                inp_func = lambda a: +_coerce(a),
	                identity_func = lambda a: 0 if known_coerce(a, 0) else None,
	                ),
}
oper_priorities.update({
	opers['__pow__'] : 0,  opers['__rpow__'] : 0, 
	opers['__pos__'] : 1, 
	opers['__neg__'] : 1, 
	opers['__invert__'] : 1, 
	opers['__mul__'] : 2, opers['__rmul__'] : 2,
	opers['__truediv__'] : 2, opers['__rtruediv__'] : 2,
	opers['__mod__'] : 2, opers['__rmod__'] : 2,
	opers['__floordiv__'] : 2, opers['__rfloordiv__'] : 2,
	opers['__add__'] : 3, opers['__radd__'] : 3,
	opers['__sub__'] : 3, opers['__rsub__'] : 3,
})




















