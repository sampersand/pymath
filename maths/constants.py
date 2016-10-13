from pymath import var
import math
class math_var(var):
	def __init__(self: 'var', value, name) -> None:
		super().__init__(value, name)
	def __str__(self):
		return self.name

e = math_var(math.e, 'e')
pi = math_var(math.pi, 'pi') #π 
