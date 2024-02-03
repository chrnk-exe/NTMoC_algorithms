from base.phi import phi
from numpy import gcd
from base.inverse import inv

# x^degree = basis mod module
def is_nth_euler_criterion(degree, basis, module):
	print(f'{basis}^(({phi(module)})/gcd({phi(module)},{degree}))')
	print(basis ** (phi(module) // gcd(phi(module), degree)) % module)
	return basis ** (phi(module) // gcd(phi(module), degree)) % module == 1

# x ** n = a mod p
def tonelli_shanks_generalized(n, a, p):
	pass

# for i in range(13):
# 	print(i, i ** 5 % 13)

# print(is_nth_euler_criterion(5, 2, 13), gcd(12, 5), 2 ** 12 % 13)
print(inv(7, 23))
print(is_nth_euler_criterion(3, 22, 43))

print('123')
