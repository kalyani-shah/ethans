def smartdiv(func):
	def inner(a,b):
		if a<b:
			return func(b,a)
		return func(a,b)
	return inner