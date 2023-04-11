from base.factorization import factor
from base.checking_for_simplicity import IsPrime
from numpy import gcd
from Logarithm.gelfond_shenks import ind
from base.get_prime_root import get_prime_root, get_all_primitive_roots
from base.inverse import inv
from base.phi import phi
from Calculators.fast_pow import degree as fast_pow
from base.ord import get_number_by_order


# x^degree = basis mod module, returns basis is nth_reduce
def is_nth_euler_criterion(degree, basis, module):
	return fast_pow((module - 1) // gcd(module - 1, degree), basis, module) == 1


# Проверка по критерию СДС, что нод степени и p - 1 должно делить
# дискретный логарифм по основанию первообразного корня а по модулю p
# возможно лучше использовать обобщённый критерий эйлера, он работает всегда, хоть и немного сложен
def is_solvable(n, a, m):
	d = gcd(n, m - 1)
	if d < 0:
		raise OverflowError('Use your own GCD, np.gcd() is overflowed')
	return ind(get_prime_root(m), a, m) % d == 0


# n is reduced modulo phi of the modulo function (n < m)
# m, n is simple
# ! a coprime with m !
# comparison is solvable
# returns x that is a modulo m to the power of n
def nthroot_tonelli_shanks_generalized(n, a, m, show_how_much_steps=False):
	d = gcd(n, m - 1)
	if d == 1:
		if show_how_much_steps:
			print('Easy Two step')
		q = (-1 * inv(n * ((m - 1) // n) + ((m - 1) % n), n)) % n
		x0 = (a ** (((m - 1) * q + 1) // n)) % m
		return x0
	else:
		# it means that d = n is prime and n | m - 1 (n <= m - 1)
		# one step
		if (((m - 1) // n) + 1) % n == 0:
			if show_how_much_steps:
				print('One step')
			return (a ** (((m - 1) // n + 1) // n)) % m
		# two-step
		elif (m - 1) // n % n != 0:
			if show_how_much_steps:
				print('Hard two step')
			qn = ((m - 1) // n) // n
			rn = (m - 1) // n % n
			q = (-1 * inv(n * qn + rn, n)) % n
			return (a ** (((m - 1) // n * q + 1) // n)) % m
		# three-step, n^2 | m - 1
		else:
			c = (a ** ((m - 1) // (n ** 2))) % m
			g = get_prime_root(m)
			if show_how_much_steps:
				print('Many step')
			if c == 1:
				# y = 0
				a_deg = (m - 1) // n ** 2
				free_deg = (m - 1)
				return tonelli_shanks_steps(a_deg, free_deg, n, a, m, g)
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
			return tonelli_shanks_steps(a_deg, free_deg, n, a, m, g)


def tonelli_shanks_steps(a_deg, free_deg, n, a, m, g):
	while (a_deg + 1) % n != 0:
		if a_deg < n:
			# calculating z, like q in two-step, then two-step solution
			z = -inv(a_deg, n) % n
			a_deg *= z
			free_deg *= z
			return (a ** ((a_deg + 1) // n) * g ** (free_deg // n)) % m
		a_deg //= n
		free_deg //= n
		# тут кроме -1 может получится любой невычет из 1, не только -1, надо наверн пока закинуть что есть, если
		# появится уравнение, где эта вещь не -1, то надо будет узнать, как найти обратный к правой части все дела и
		# домножать на него
		if ((a ** a_deg) * (g ** free_deg)) % m == -1:
			free_deg += (m - 1) / 2
	return (a ** ((a_deg + 1) // n) * g ** (free_deg // n)) % m


# x^n = a mod m, x = root
def find_all_roots_by_root(n, a, m, root):
	result = [root]
	if gcd(n, m - 1) == 1:
		return result
	else:
		delta = get_number_by_order(n, m)
		for i in range(1, n):
			result.append(root * (delta ** i) % m)
		return sorted(result)


def tonelli_shanks_steps_count(n, a, m):
	if not is_nth_euler_criterion(n, a, m):
		return 'not solvable'
	d = gcd(n, m - 1)
	if d == 1:
		return 'Easy Two step'
	if (((m - 1) // n) + 1) % n == 0:
		return 'One step'
	elif (m - 1) // n % n != 0:
		return 'Hard two step'
	else:
		return 'Many step'
# x^20 = 4 mod 23 (x1 = 11, x2 = 12)
# list of args [n, a, m]
# tests
args = [
	[3, 15, 31],  # two-step hard
	[2, 23, 41],  # many step
	[2, 46, 73],  # many step
	[7, 17, 53],  # two-step easy
	[5, 29, 61],  # two-step hard
	[3, 22, 43],  # one step
	[3, 7, 19],  # many step
	[5, 6, 101],  # many step
	[7, 6, 197],  # many step
	[5, 2, 13]  # two-step easy
]


for arg in args:
	print('------------------------------------------')
	print(f'Solving x^{arg[0]} = {arg[1]} mod {arg[2]}')
	print(f"Euler criterion: {is_nth_euler_criterion(*arg)}")
	print(f'Steps count: {tonelli_shanks_steps_count(*arg)}')
	print(f'Count of roots: gcd({arg[0]}, {arg[2] - 1}) = {gcd(arg[0], arg[2] - 1)}')
	ans = nthroot_tonelli_shanks_generalized(*arg)
	assert ans ** arg[0] % arg[2] == arg[1], f'{arg} error!'
	print(f'All Roots: {find_all_roots_by_root(*[*arg, ans])}, first root: {ans}')

