from numpy import gcd, abs
import pandas as pd


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


# отображение берётся f(x) = Rm(x^2 + 1)
# можно брать любое а КРОМЕ 0 и -2
def f(x, m, a=1):
	return (x * x + a) % m


# x0 = y0 = 2
def rho_floyd_pollard(n, x0=2, y0=2):
	df = pd.DataFrame(
		data={
			'x_i': [], 'y_i': [], 'd_i': []
		}
	)
	# x0 = y0 = 2
	while True:
		x0 = f(x0, n)
		y0 = f(f(y0, n), n)

		df.loc[len(df)] = [x0, y0, g := gcd(abs(x0 - y0), n)]
		if g != 1:
			break
	print(df)
	return gcd(abs(x0 - y0), n)


a = rho_floyd_pollard(n := int(input('Введите число для факторизации: ')))
print(f"\n{a} * {n // a}")
