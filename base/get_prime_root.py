from base.phi import phi
from base.ord import get_number_by_order


def get_prime_root(m):
	return get_number_by_order(phi(m), m)


def get_all_primitive_roots(m):
	return get_number_by_order(phi(m), m, 1)
