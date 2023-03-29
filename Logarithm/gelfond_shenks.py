import math
from Calculators.fast_pow import degree


# возвращает класс вычетов x по модулю m - 1, где a ^ x == b (mod m)
# стоит переделать, тк эта версия не оптимальна по памяти
# x = ind_a (b) mod m
def ind(basis, free_member, module):
	# print(basis, free_member, module)
	e = int(math.sqrt(module)) + 1
	ae = degree(e, basis, module)
	cy = []
	dz = []
	for i in range(1, e):
		cy.append((ae ** i) % module)
		dz.append((free_member * (basis ** i)) % module)
		if len(set.intersection(set(cy), set(dz))) > 0:
			temp = list(set.intersection(set(cy), set(dz)))[0]
			y = cy.index(temp) + 1
			z = dz.index(temp) + 1
			return (e * y - z) % (module - 1)
