from numpy import sqrt


def factorization(n):
	s = int(sqrt(n)) + 1
	# а по факту надо k до бесконечности перебирать
	for k in range(1, n):
		y = (s+k) ** 2 - n
		sqrty = sqrt(y)
		if sqrty == int(sqrty):
			break
	else:
		return [0, 0]
	return list(map(int, [s+k+sqrty, s+k-sqrty]))


print(factorization(89755))
