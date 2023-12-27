

def extendEuclid(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = extendEuclid(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q
    
def crt1(PairPrimes, PairRest):
    m1, m2 = PairPrimes
    r1, r2 = PairRest
    x, y, q = extendEuclid(m1, m2)
    _, _, _q = extendEuclid(r1, r2)
    print(m1, m2, r1, r2)
    assert _q % q == 0
    if q != 1:
        return crt1([m1 // q, m2 // q], [r1 // q, r2 // q])
    else:
        return (r1 * y * m2 + r2 * x * m1) % (m1 * m2), m1 * m2

def crt(PairPrimes, PairRest):
    assert len(PairPrimes) == len(PairRest)
    rest, mod = crt1(PairPrimes[:2], PairRest[:2])
    for i in range(2, len(PairPrimes)):
        rest, mod = crt1([mod, PairPrimes[i]], [rest, PairRest[i]])
    return rest, mod
       
