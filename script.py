def sum(a,b):
	return a + b

def divide(a,b):
	if b == 0:
		raise ValueError("can't divide by zero")
	return a/b
	if isinstance(a,list) or isinstance(b,list):
		raise ValueError("can't divide list)

