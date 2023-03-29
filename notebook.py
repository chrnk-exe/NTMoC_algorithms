from Calculators.fast_pow import degree as fast_pow
from base.Legengre import Legendre
from base.get_system import get_reduced_system
from base.checking_for_simplicity import IsPrime
from base.phi import phi
from numpy import gcd
from base.inverse import inv
from Logarithm.gelfond_shenks import ind
from base.get_prime_root import get_prime_root


def mod_pow(basis, degree, module):
	return basis ** degree % module



def square_AMM(delta, module):
	if Legendre(delta, module) == -1 or not IsPrime.D_stupid_is_prime(module):
		return None

	reduced_system = get_reduced_system(module)

	# rho is random_non_quadratic_residue
	rho = 0
	for item in reduced_system:
		if Legendre(item, module) == -1:
			rho = item
			break
	else:
		print('There is no quadratic residue in reduced system, idk what to do!!!')
		return None

	s, t = module - 1, 0
	while s % 2 == 0:
		s //= 2
		t += 1

	a = mod_pow(rho, s, module)
	b = mod_pow(delta, s, module)
	h = 1

	for i in range(1, t):
		d = b ** (2 ** (t - 1 - i))
		k = 0 if d == 1 else 1
		b = b * (a ** 2*k)
		h = h * (a ** k)
		a **= 2

	return (delta ** ((s + 1) // 2) * h) % module


# https://encyclopediaofmath.org/wiki/Euler_criterion
# http://hackmat.se/kurser/TATM54/booktot.pdf page 76 (88)
def is_nth_euler_criterion(degree, basis, module):
	return basis ** (phi(module) // gcd(phi(module), degree)) % module == 1


# надо найти алгоритм вычисления nth - вычета
# x^r = delta (mod m)
def rth_root_AMM(r, delta, module):
	if not is_nth_euler_criterion(r, delta, module) or not IsPrime.D_stupid_is_prime(module):
		return None

	if gcd(r, module - 1) == 1:
		return delta ** inv(r, module) % module
	elif module - 1 % r != 0:
		print('Так быть не должно! Китайцы не могут врать!')
		return None

	reduced_system = get_reduced_system(module)
	rho = 0
	for item in reduced_system:
		if item ** ((module - 1) // r) != 1:
			rho = item
			break
	else:
		print(f'There is no {r}th residue in reduced system, idk what to do!!!')
		return None

	s, t = module - 1, 0

	while gcd(s, r) != 1:
		s //= r
		t += 1

	alpha = 1
	while (r * alpha - 1) % s != 0:
		alpha += 1

	a = mod_pow(rho, s * r ** (t - 1), module)
	b = mod_pow(delta, r * alpha - 1, module)
	c = mod_pow(rho, s, module)
	h = 1
	for i in range(1, t - 1):
		d = mod_pow(b, r ** (t - 1 - i), module)
		j = 0 if d == 1 else -ind(a, b, module)
		b *= (c ** (r * j))
		h *= c ** j
		c **= r

	return (delta ** alpha) * h % module


# print(rth_root_AMM(5, 3, 13), 9 ** 5 % 13) # x^2 = 10 mod 13


def rth_root_Anna(q, s, p):
	r, delta, module = q, s, p
	if not is_nth_euler_criterion(r, delta, module) or not IsPrime.D_stupid_is_prime(module):
		return None

	g = get_prime_root(p)
	if g is None:
		return None
	h = (p - 1) // q
	while h % q == 0:
		h //= q
	# return
	z = h * (-inv(h, q))
	x = (z + 1) // q

	v = mod_pow(s, x, p)

	t = ind(g ** (h*q), s ** h, p)

	return v * g ** (-z * t)

#
print(rth_root_Anna(5, 2, 13), 9 ** 5 % 13) # x^2 = 10 mod 13
