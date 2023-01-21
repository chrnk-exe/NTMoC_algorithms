from base.factorization import factor
from base.stupid_is_prime import is_prime
from numpy import gcd
from gelfond_shenks import ind
from base.get_prime_root import get_prime_root


# Проверка по критерию СДС, что нод степени и p - 1 должно делить
# дискретный логарифм по основанию первообразного корня а по модулю p
def is_solvable(n, a, m):
	d = gcd(n, m - 1)
	if d < 0:
		raise OverflowError('Use your own GCD, np.gcd() is overflowed')
	return ind(get_prime_root(m), a, m) % d == 0


# power binomial comparison
def solve_pbc(n, a, m):
	if not is_prime(m):
		modules = factor(m)
		a = [a % module for module in modules]
		result = []
		for i in range(len(modules)):
			result.append(solve_pbc(n, a[i], modules[i]))
	else:
		# Также необходимо проверить, является ли СДС разрешимым. Оно сюда дойдёт уже с простым модулем, так что всё ок
		if not is_solvable(n, a, m):
			print("Сравнение неразрешимо по критерию СДС")
		# для простоты пока m - простое
		# понять сколько шагов для начала
		R = ((m-1) ** 2) % n
		if ((m-1) // n) % n == n - 1:
			print('One step')
			one_step(n, a, m)
		elif n % ((m - 1) // n) == 0:
			print('Two step')
		else:
			print('Many steps')


def one_step(n, a, m):
	deg = (m-1) // n
	x0 = a ** ((deg + 1) // n) % m
	return x0


solve_pbc(7, 17, 53)

