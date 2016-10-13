import pymath
class system(dict, pymath.pymath_obj):
	def __setattr__(self, attr, value):
		if attr in self:
			if isinstance(value, pymath.var):
				self[attr].set(value)
		else:
			if isinstance(value, pymath.pymath_obj):
				value.name = attr
				self[attr] = value
			else:
				self[attr] = pymath.var(value = value)
	def __getattr__(self, attr):
		return self[attr]

	def get(self, *args):
		return (self[arg] for arg in args)
