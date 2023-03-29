from numpy import gcd


def get_reduced_system(n):
	return [i for i in range(n) if gcd(i, n) == 1]


def get_full_system(n):
	return [i for i in range(n)]

