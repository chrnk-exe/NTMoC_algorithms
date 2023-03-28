from pprint import pprint

class Karatsuba:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.steps = list()

    def solve(self):
        self.karatsuba(self.a, self.b)
        return self.steps[::-1]

    def karatsuba(self, a, b):
        if len(str(a)) == 1 and len(str(b)) == 1:
            return a * b
        la, lb = len(str(a)), len(str(b))
        if la % 2 != 0 and lb % 2 != 0 and la == lb:
            if la > lb:
                la += 1
            else:
                lb += 1

        n = int(max(la, lb) // 2)
        a1 = a // (10 ** n)
        b1 = b // (10 ** n)
        a_value = self.karatsuba(a1, b1)
        a0 = a % (10 ** n)
        b0 = b % (10 ** n)
        b_value = self.karatsuba(a0, b0)
        ta = a0 + a1
        tb = b0 + b1
        c = self.karatsuba(ta, tb)
        result = (10 ** (2 * n)) * a_value + (10 ** n) * (c - a_value - b_value) + b_value
        self.steps.append({
            'label': f'Выолним умножение {a} на {b}',
            'type': 'matrix',
            'data': [['a', 'b', 'n', 'A1', 'B1', 'A', 'A0', 'B0', 'B', 'tA', 'tB', 'C', 'Ответ'], [a, b, n, a1, b1, a_value, a0, b0, b_value, ta, tb, c, result]]
        })
        return result

