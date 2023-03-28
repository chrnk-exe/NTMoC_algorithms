from random import randint
from Calculators.bin_gcd import bin_gcd
from Calculators.fast_pow import degree
from base.Jacobi_symbol import Jacobi


class IsPrime:
    @staticmethod
    def D_stupid_is_prime(n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n

    @staticmethod
    def P_Fermat(n):
        if n < 5:
            return None
        a = randint(2, n-2)
        r = a ** (n - 1) % n
        return r == 1

    @staticmethod
    def P_Solovay_Strassen(n, k, show_probability=False):
        if n < 2:
            return None
        for i in range(k):
            a = randint(2, n-1)
            if bin_gcd(a, n) > 1:
                return False
            if a ** ((n - 1) // 2) % n != Jacobi(a, n) % n:
                return False
        return [True, 1 - 2 ** (-k)] if show_probability else True

    @staticmethod
    def P_Miller_Rabin(n ,k, show_probability=False):
        t, s = n - 1, 0
        while t % 2 == 0:
            t //= 2
            s += 1
        for i in range(k):
            a = randint(2, n-2)
            x = degree(t, a, n)
            if x == 1 or x == n - 1:
                continue
            for j in range(s-1):
                x = (x ** 2) % n
                if x == 1:
                    return False
                if x == n - 1:
                    break
            else:
                return False
        return [True, 1 - 4 ** (-k)] if show_probability else True

    # Lucas-Lehmer test
    @staticmethod
    def D_LLT(p):
        s = 4
        k = 1
        m = (2 ** p) - 1
        while k != p - 1:
            s = (s ** 2 - 2) % m
            k += 1
        return s == 0

    # хуй знает нашёл этот метод в книжке нихуя не понятно
    @staticmethod
    def P_generate(k, t):
        if t < 1:
            return None
        while True:
            # Generate Random kbit number
            numbers = [1]
            for i in range(k - 2):
                numbers.append(randint(0, 1))
            numbers.append(1)
            p = 0
            for i in range(k):
                p += numbers[i] * (2 ** i)

            # Отсекает много непригодных чисел
            if any([p % 3 != 0, p % 5 != 0, p % 7 != 0]):
                continue

            # Тут надо t раз проверить число на простоту по основанию a алгоритмом Рабина, но что такое "по основанию а"
            # я не понял
            for i in range(t):
                a = randint(2, p-2)



