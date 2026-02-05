def sum(a,b):
	return a + b

def divide(a,b):
	if b == 0:
		raise ValueError("can't divide by zero")
	return a/b
