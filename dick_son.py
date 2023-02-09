import math

from algorithms.fast_pow import fast_pow


def decompose_to_primes(number):
    response = {}
    divider = 2

    while number > 1:
        while number % divider == 0:
            number //= divider
            response[divider] = response.get(divider, 0) + 1
        divider += 1
    return response


def is_smooth(number, r):
    return all(i <= r for i in decompose_to_primes(number).keys())


def search_a_smooth_square_for_module(module, r):
    for i in range(1, 2000):
        number = fast_pow(2, i, module, onlyResult=True)

        if is_smooth(number, r):
            ans = math.sqrt(number)
            if ans % 1 == 0:
                ans = int(ans)
                if ans != i:
                    gcd = math.gcd(module, i - ans)
                    print(f'{i} != {ans}', '|', f'{gcd} * {module/gcd}')
                    # return


s = search_a_smooth_square_for_module(3127, 5)
