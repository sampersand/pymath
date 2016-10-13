from pymath import pymath_obj
from pymath.defaults.functions.seeded_func import seeded_func
class default_func(pymath_obj):

	seeded_type = seeded_func

	def __init__(self, inp_func, name = '??', args_strs = None, body_str = '??'):
		super().__init__(name)
		self.inp_func = inp_func
		self.args_strs = args_strs if args_strs != None else tuple('??' for x in range(self.req_arg_count))
		self.body_str = body_str

	@property
	def req_arg_count(self):
		return self.inp_func.__code__.co_argcount

	def _def_str(self, print_args):
		if __debug__:
			assert len(print_args) == self.req_arg_count #not required, just why would you do it otherwise?
		return '{}({})'.format(self.name, ', '.join(str(a) for a in print_args))


	def __str__(self):
		return self._def_str(self.args_strs) + ' = ' + self.body_str

	def __call__(self, *arguments) -> seeded_type:
		if __debug__:
			assert len(arguments) == self.req_arg_count, 'Incorrect amoutn of arguments for: ' + str(self)
		return self.seeded_type(self, arguments)

	def __repr__(self, full = False):
		if full:
			return '{}({}{}{}{})'.format(type(self).__qualname__, repr(self.inp_func),
		                             ', ' + self.name if self.name != '??' else '',
		                             ', ' + repr(self.args_strs) if self.args_strs != None and any(x != '??' for x in self.args_strs) else '',
		                             ', ' + self.body_str if self.body_str != '??' else '',

		                             )
		return '{}({})'.format(type(self).__qualname__, 
		                             *', '.join(x for x in {
		                                        str(self.name) if self.name != '??' else None,
		                                        str(self.args_strs) if self.args_strs != None and any(x != '??' for x in self.args_strs) else None,
		                                    	str(self.body_str) if self.body_str != '??' else None
		                                        }
		                                        if x != None)
		                             )