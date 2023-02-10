from pbc.shenks import is_solvable
# Это решает только уравнения вида x^2 = n mod p

def Legendre(a, p):
	if a % p == 0:
		return 0
	elif a ** ((p-1) // 2) % p == 1:
		return 1
	else:
		return -1

#x^2 = n mod p
def solve_pbc(n, p):
	if not is_solvable(2, n, p):
		return None
	print('Сравнение разрешимо')
	S = 0
	new_p = p - 1
	while new_p % 2 == 0:
		S += 1
		new_p //= 2
	Q = (p-1) // (2 ** S)
	if S == 1:
		return [n ** ((p + 1) // 4), -n ** ((p + 1) // 4)]
	c = 0
	for z in range(2, p-1):
		if Legendre(z, p) == -1:
			c = (z ** Q) % p
			break
	R = n ** ((Q + 1) / 2) % p
	t = n ** Q % p
	M = S
	while t % p != 1:
		I = 0
		for i in range(M):
			if t ** (2 ** i) % p == 1:
				I = i
				break
		b = (c ** (2 ** (M - I - 1))) % p
		R = (R * b) % p
		t = (t * b * b) % p
		c = (b ** 2) % p
		M = I
	return [int(R), int(p - R)]


print(solve_pbc(10, 13))
