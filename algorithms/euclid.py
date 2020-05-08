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
