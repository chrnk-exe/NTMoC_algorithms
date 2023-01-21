from base.lcm import lcm as M
from base.phi import phi
from base.factorization import factorization


def factor(n):
	return list(factorization(n).iloc[:, 1])


def L(m):
	temp = list(map(phi, factor(m)))
	return M(*temp)

