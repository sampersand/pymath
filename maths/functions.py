from pymath.defaults.functions import seeded_func, default_func
import math



class math_ln(default_func):
	class seeded_math_ln(seeded_func):
		def __init__(self, func_instance, args_to_pass_to_func):
			super().__init__(func_instance, args_to_pass_to_func)

		def deriv(self, du):
			return self[0].deriv(du) / self[0]

	seeded_type = seeded_math_ln
	def __init__(self):
		super().__init__(math.log, 'ln', 'x', 'ln(x)')

	@property
	def req_arg_count(self):
		return 1

ln = math_ln()