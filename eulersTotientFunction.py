from fractions import gcd
def eulersTotientFunction(n):
    return len([x for x in range(n) if gcd(x,n) == 1])

