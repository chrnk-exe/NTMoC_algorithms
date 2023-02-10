import math
from base.fast_pow import degree
from base.add_double import mult


# возвращает класс вычетов x по модулю m - 1, где a ^ x == b (mod m)
# стоит переделать, тк эта версия не оптимальна по памяти
def ind(a, b, m):
	print(a, b, m)
	e = int(math.sqrt(m)) + 1
	ae = degree(e, a, m, 1)
	cy = []
	dz = []
	for i in range(1, e):
		cy.append((ae ** i) % m)
		dz.append((b * (a**i)) % m)
		if len(set.intersection(set(cy), set(dz))) > 0:
			temp = list(set.intersection(set(cy), set(dz)))[0]
			y = cy.index(temp) + 1
			z = dz.index(temp) + 1
			return (e * y - z) % (m - 1)
