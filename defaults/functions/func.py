import re, inspect
from pymath.defaults.functions import default_func
class func(default_func):
	lambda_regex = re.compile(r'''(?x)
	                          (?P<name>\w+)\s*=\s*
	                          (?:func|\w+)[(]
                          		lambda\s+
                          			(?P<args_strs>
                          				(?:\w+\s*,?\s*)*
                          			)
	                          	\s*:\s*(?P<body_str>.*)[)]\s*$
	                          ''')

	def __init__(self, inp_func):
		super().__init__(inp_func, **func._find_func_strs(inp_func))

	@staticmethod
	def _find_func_strs(inp_func):
		match = func.lambda_regex.search(inspect.getsource(inp_func))
		if __debug__:
		    assert match != None, 'No string match found! try using the default_func class!'
		ret = match.groupdict()
		ret['args_strs'] = ret['args_strs'].replace(' ', '').split(',')
		return ret