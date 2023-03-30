from base.lcm import lcm as M
from base.phi import phi
from base.factorization import factorization, factor


def L(m):
	temp = list(map(phi, factor(m)))
	return M(*temp)

