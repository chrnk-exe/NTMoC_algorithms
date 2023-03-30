from base.get_prime_root import get_prime_root as primitive_root
from base.checking_for_simplicity import IsPrime
from base.phi import phi
from numpy import gcd
from Calculators.ext_bin_gcd import ext_bin_gcd as igcdex
from Logarithm.gelfond_shenks import ind


def is_nth_euler_criterion(degree, basis, module):
	return basis ** (phi(module) // gcd(phi(module), degree)) % module == 1


# x ** q = s mod p
def nthroot(q, s, p, all_roots):
	if not is_nth_euler_criterion(q, s, p) or not IsPrime.D_stupid_is_prime(q):
		return None

	g = primitive_root(p)

	f = p - 1
	assert (p - 1) % q == 0
	# determine k
	k = 0
	while f % q == 0:
		k += 1
		f = f // q
	# find z, x, r1
	f1 = igcdex(f, q)[0] % q
	z = f * f1
	x = (1 + z) // q
	r1 = pow(s, int(x), p)
	s1 = pow(s, f, p)
	h = pow(g, f * q, p)
	t = ind(s1, h, p)
	g2 = pow(g, int(z * t), p)
	g3 = igcdex(g2, p)[0]
	r = r1 * g3 % p
	# assert pow(r, q, p) == s
	res = [r]
	h = pow(g, (p - 1) // q, p)
	# assert pow(h, q, p) == 1
	hx = r
	for i in range(q - 1):
		hx = (hx * h) % p
		res.append(hx)
	if all_roots:
		res.sort()
		return res
	return min(res)


print(nthroot(5, 6, 31, 1))

