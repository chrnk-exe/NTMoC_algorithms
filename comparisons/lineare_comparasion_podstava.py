from base.inverse import inv
from base.factorization import factor
from chinese_theorem import get_solution
# from numpy import gcd
from Calculators.many_gcd import gcd


def solve_linear_comparison(a, b, m):
	inverse = inv(a, m)
	if inverse:
		return b * inverse % m
	else:

		divider = gcd(a, b, m)
		a = a // divider
		b = b // divider
		m = m // divider

		# Критерий линейного сравнения
		d = gcd(a, m)
		if b % d != 0:
			print('Решений нет')
			return False
		modules = list(set(factor(m)))
		new_b = [b % m for m in modules]
		for i in range(len(modules)):
			if a % modules[i] != 1:
				new_b[i] *= inv(a, modules[i])
		return get_solution(new_b, modules)


print(solve_linear_comparison(4, 20, 30))
