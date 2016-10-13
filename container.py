from pymath import pymath_obj
class pymath_container(pymath_obj):
	def __init__(self, iterable, name = None):
		super().__init__(name = name)
		self._iterable = iterable

	def __iter__(self):
		return iter(self._iterable)

	@property
	def known(self):
		return all(ele.known for ele in self)

	def __getitem__(self, item):
		return self._iterable[item]