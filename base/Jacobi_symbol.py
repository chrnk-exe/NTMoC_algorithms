from base.Legengre import Legendre
from base.factorization import factor


def Jacobi(a, P):
	p = factor(P)
	result = 1
	for i in p:
		result *= Legendre(a, i)
	return result
