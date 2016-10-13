import pymath
class pymath_obj():
	def __init__(self, name = None, value = None):
		self._name = name
		self._value = value

	@property
	def known(self):
		return self.value != None

	@property
	def hasname(self) -> bool:
		return self._name != None

	def value():
	    def fget(self):
	        return self._value
	    def fset(self, value):
	        self._value = value
	    return locals()
	value = property(**value())

	def name():
		def fget(self):
			return str(self._name) if self.hasname else '{unnamed ' + type(self).__qualname__ + '}'
		def fset(self, value):
			self._name = value
		return locals()
	name = property(**name())

	# @property
	# def value(self):
	# 	print('Warning! Value for \'{}\' not known!'.format(self.name))
	# 	return None

	def deriv(self, differ):
		return 0


	def __bool__(self) -> bool: return bool(self.value)
	def __int__(self) -> int: return int(self.value)
	def __float__(self) -> float: return float(self.value)
	def __complex__(self) -> complex: return complex(self.value)

	def __add__(self, other): return pymath.defaults.functions.oper.opers['__add__'](self, other)
	def __sub__(self, other): return pymath.defaults.functions.oper.opers['__sub__'](self, other)
	def __mul__(self, other): return pymath.defaults.functions.oper.opers['__mul__'](self, other)
	def __truediv__(self, other): return pymath.defaults.functions.oper.opers['__truediv__'](self, other)
	def __floordiv__(self, other): return pymath.defaults.functions.oper.opers['__floordiv__'](self, other)
	def __pow__(self, other): return pymath.defaults.functions.oper.opers['__pow__'](self, other)
	def __mod__(self, other): return pymath.defaults.functions.oper.opers['__mod__'](self, other)

	def __lt__(self, other): return pymath.defaults.functions.oper.opers['__lt__'](self, other)
	def __gt__(self, other): return pymath.defaults.functions.oper.opers['__gt__'](self, other)
	# def __eq__(self, other): return pymath.defaults.functions.oper.opers['__eq__'](self, other)
	# def __ne__(self, other): return pymath.defaults.functions.oper.opers['__ne__'](self, other)
	def __ge__(self, other): return pymath.defaults.functions.oper.opers['__ge__'](self, other)
	def __le__(self, other): return pymath.defaults.functions.oper.opers['__le__'](self, other)

	def __eq__(self, other): 
		if not isinstance(other, pymath_obj):
			return self.known and self.value == other
		elif self is other:
			return True
		else:
			return not (self.known ^ other.known) and (self.known and (self.value == other.value))
	def __ne__(self, other):
		return not(self == other)

	def __radd__(self, other): return pymath.defaults.functions.oper.opers['__radd__'](self, other)
	def __rsub__(self, other): return pymath.defaults.functions.oper.opers['__rsub__'](self, other)
	def __rmul__(self, other): return pymath.defaults.functions.oper.opers['__rmul__'](self, other)
	def __rtruediv__(self, other): return pymath.defaults.functions.oper.opers['__rtruediv__'](self, other)
	def __rfloordiv__(self, other): return pymath.defaults.functions.oper.opers['__rfloordiv__'](self, other)
	def __rpow__(self, other): return pymath.defaults.functions.oper.opers['__rpow__'](self, other)

	def __neg__(self): return pymath.defaults.functions.oper.opers['__neg__'](self)
	def __pos__(self): return pymath.defaults.functions.oper.opers['__pos__'](self)
	def __invert__(self): return pymath.defaults.functions.oper.opers['__invert__'](self)
	
	def __repr__(self: 'pymath_obj') -> str:
		return '{}()'.format(type(self).__qualname__)
