from numpy import gcd
from base.inverse import inv


def get_solution(a, modules):
	for i in range(len(modules)):
		for j in range(i + 1, len(modules)):
			if gcd(modules[i], modules[j]) != 1:
				print('Error! Modules must be coprime!')
				return -1
	M = 1
	for i in modules:
		M *= i
	mi = []
	for i in modules:
		mi.append(M // i)
	N = []
	for i in range(len(modules)):
		N.append(inv(mi[i], modules[i]))
	result = sum([mi[i] * N[i] * a[i] for i in range(len(modules))])

	prod = 1
	for module in modules:
		prod *= module
	return result % prod
