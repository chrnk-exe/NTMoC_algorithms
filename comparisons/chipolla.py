from base.Legengre import Legendre
from base.checking_for_simplicity import IsPrime
from base.factorization import factor
from math import sqrt


# x^2 = a (mod m)
def solve_pbc(a, m):
	if not IsPrime.D_stupid_is_prime(m):
		modules = factor(m)
		a = [a % module for module in modules]
		result = []
		for i in range(len(modules)):
			result.append(solve_pbc(a[i], modules[i]))
		return result
	else:
		n = 0
		for i in range(2, m):
			if Legendre(i ** 2 - a, m) == -1:
				n = i
				break
		# x = (n + sqrt(n ** 2 - a))**((m+1)//2)
		print(f'({n} + sqrt({n ** 2 - a}) ^ ({(m + 1)//2})')

solve_pbc(10, 13)
