from bin_gcd import bin_gcd


def gcd(*args):
	result = 1
	for arg in args:
		result = bin_gcd(result, arg)
	return result
