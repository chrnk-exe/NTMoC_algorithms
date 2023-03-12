from Legengre import Legendre
from factorization import factor


def Jacobi(a, P):
	p = factor(P)
	result = 1
	for i in p:
		result *= Legendre(a, i)
	return result
