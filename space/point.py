import pymath
class point(list, pymath.pymath_obj):
	def __new__(self, *args):
		return super().__new__(self, [])
	def __init__(self, *args):
		super().__init__(args)
	def __str__(self):
		return str(tuple(self))