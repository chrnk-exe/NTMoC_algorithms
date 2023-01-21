import pandas as pd


def factorization(n, output=False):
    df = pd.DataFrame(columns=['n', 'prime'])
    if output:
        print(f"Факторизуем число {n} (разложим на произведение простых чисел)")

    prime = 2
    while prime < n:
        if n % prime == 0:
            df = df.append(
                    {
                        'n': int(n),
                        'prime': int(prime)
                    },
                    ignore_index=True
                 )
            n /= prime
            continue

        prime += 1

    df = df.append(
             {
                'n': int(n),
                'prime': int(n)
             },
             ignore_index=True
         )


    if output:
        print(df)
        print()

    return df


def factor(n):
    return list(factorization(n).iloc[:, 1])

