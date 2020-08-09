from functools import reduce


def euclid(a: int, b: int) -> int:
    return a if not b else euclid(b, a % b)


def extended_euclid(a: int, b: int) -> (int, int, int):
    """
    Finds x and y where
    ax+by=gcd(a,b)
    """
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    g, x, y = extended_euclid(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def crt(n, N, a):
    result = 0
    for i in range(len(n)):
        ai = a[i]
        ni = n[i]
        _, _, si = extended_euclid(ni, N // ni)
        result += ai * si * (N // ni)
    return result, N


def crt(a, n):
    conds = {a_: n_ for a_, n_ in zip(a, n)}
    print(conds)
    product = reduce(lambda x, y: x * y, conds.values())
    sequences = [set(range(a, product, n)) for a, n in conds.items()]
    result = list(reduce(lambda x, y: x & y, sequences))
    return result

