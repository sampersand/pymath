# def has_attr(arg, attr, *args):
# 	return not hasattr(arg, attr) or (getattr(arg, attr) if not args else getattr(arg, attr)(*args))

def known(arg):
	return not hasattr(arg, 'known') or arg.known

def value(arg):
	return arg.value if hasattr(arg, 'value') else arg
# def known_coerce(arg, *tocomp):
# 	return known(arg) and coerce(arg) in tocomp
def coerce_deriv(obj, du):
	return 0 if not hasattr(obj, 'deriv') else obj.deriv(du)
	
# def known(arg):
# 	return not hasattr(arg, 'known') or arg.known
# def coerce(arg):
# 	return arg.value if hasattr(arg, 'value') else arg
# def known_coerce(arg, *tocomp):
# 	return known(arg) and coerce(arg) in tocomp
def is_constant(obj, du_list):
	return not hasattr(arg, 'is_constant') or arg.is_constant(du_list)
