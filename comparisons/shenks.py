from base.factorization import factor
from base.checking_for_simplicity import IsPrime
from numpy import gcd
from Logarithm.gelfond_shenks import ind
from base.get_prime_root import get_prime_root, get_all_primitive_roots
from base.inverse import inv
from base.phi import phi


# Проверка по критерию СДС, что нод степени и p - 1 должно делить
# дискретный логарифм по основанию первообразного корня а по модулю p
def is_solvable(n, a, m):
	d = gcd(n, m - 1)
	if d < 0:
		raise OverflowError('Use your own GCD, np.gcd() is overflowed')
	return ind(get_prime_root(m), a, m) % d == 0


# power binomial comparison, x^n = a (mod m)
def solve_pbc(n, a, m):
	if not IsPrime.D_stupid_is_prime(m):
		modules = factor(m)
		a = [a % module for module in modules]
		result = []
		for i in range(len(modules)):
			result.append(solve_pbc(n, a[i], modules[i]))
		return result

	if not is_solvable(n, a, m):
		print("Сравнение неразрешимо по критерию СДС")
		return None

	# m is simple
	# We have x^n = a (mod m), where 'a' is nth root
	d = gcd(m - 1, n)
	if d == 1:
		pass


# n is reduced modulo phi of the modulo function (n < m)
# m, n is simple
# ! a coprime with m !
# comparison is solvable
# returns x that is a modulo m to the power of n
def nthroot_tonelli_shanks_generalized(n, a, m):
	d = gcd(n, m - 1)
	if d == 1:
		print('Easy Two step')
		q = (-1 * inv(n * ((m - 1) // n) + ((m - 1) % n), n)) % n
		x0 = (a ** (((m - 1) * q + 1) // n)) % m
		return x0
	else:
		# it means that d = n is prime and n | m - 1 (n <= m - 1)
		# one step
		if (((m - 1) // n) + 1) % n == 0:
			print('One step')
			return ((a ** (m + n - 1)) // (n ** 2)) % m
		# two-step
		elif (m - 1) // n % n != 0:
			print('Hard two step')
			qn = ((m - 1) // n) // n
			rn = (m - 1) // n % n
			q = (-1 * inv(n * qn + rn, n)) % n
			return (a ** (((m - 1) * q + 1) // n)) % m
		# three-step, n^2 | m - 1
		else:
			c = (a ** ((m - 1) // (n ** 2))) % m
			g = get_prime_root(m)
			print('Many step')
			if c == 1:
				y = 0
				a_deg = (m - 1) // n ** 2
				free_deg = (m - 1)
				return tonneli_shanks_steps(a_deg, free_deg, n, a, m, g)
			y = 0
			# wtf......
			for i in range(n):
				if g**((m - 1) // n * i) % m == c:
					y = i
					break
			else:
				y = ind(g**((m - 1) // n), c, m)
			a_deg = (m - 1) // n ** 2
			free_deg = (m - 1) // n * (-y) % (m - 1)
			return tonneli_shanks_steps(a_deg, free_deg, n, a, m, g)


def tonneli_shanks_steps(a_deg, free_deg, n, a, m, g):
	while (a_deg + 1) % n != 0:
		a_deg //= n
		free_deg //= n
		if ((a ** a_deg) * (g ** free_deg)) % m == -1:
			free_deg += (m - 1) / 2

	return (a ** ((a_deg + 1) // n) * g ** (free_deg // n)) % m


# x^20 = 4 mod 23 (x1 = 11, x2 = 12)
# list of args [n, a, m]
# args = [
# 	[3, 15, 31], # two-step
# 	[2, 23, 41], # many step
# 	[2, 46, 73], # many step
# 	[7, 17, 53], # two-step
# 	[5, 29, 61], # two-step
# 	[3, 22, 43], # one step
# 	[3, 7, 19], # many step
# 	[5, 6, 101] # many step
# ]
# for arg in args:
# 	nthroot_tonelli_shanks_generalized(*arg)

# print(get_prime_root(41))
# print(get_all_primitive_roots(37), len(get_all_primitive_roots(37)) == phi(phi(37)))

# res = []
# for i in range(1, 41):
# 	res.append(i)
# 	print(2 ** i % 41)
#
# print(list(set(res)))
# print(2 ** 12 % 37)
# print(ind(26, 26, 37))
# for i in range (13):
# 	print(26 ** i % 37 == 26, i)

# print(23 ** ((41 - 1) // (2 ** 2)) % 41)
print(get_all_primitive_roots(41))
# print(get_all_primitive_roots(101))
# print(2 ** 12 % 19)
# print(ind(2 ** 6 % 19, 11, 19))
# print(11 * 2 ** 6 % 19)
# print(is_solvable(5, 6, 101))
# print(2 ** 20 % 101)
# print(ind(95, 84, 101))
# print(96 ** 5 % 101)
# print(nthroot_tonelli_shanks_generalized(5, 6, 101))
# print(nthroot_tonelli_shanks_generalized(2, 46, 73))
print(nthroot_tonelli_shanks_generalized(2, 23, 41))
# print(96 ** 5 % 101)
# print(8 ** 2 % 41)
