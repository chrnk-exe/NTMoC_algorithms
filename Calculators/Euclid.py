
def Euclid(a, b):
	result = []
	while a != b:
		if a > b:
			a -= b
		else:
			b -= a
		result.append([a, b])
	return result


