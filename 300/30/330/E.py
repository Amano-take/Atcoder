import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
8 5
2 0 2 2 1 1 2 5
4 3
4 4
6 3
8 1000000000
2 1
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()

class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (2 * self._size)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)
    
    def set(self, p, x):
        if 0 <= p < self._n:
            p += self._size
            cp, vp = self._d[p]
            self._d[p] = (cp + 1, vp)
            for i in range(1, self._log + 1):
                self._update(p >> i)
        if 0 <= x < self._n:
            x += self._size
            cp, vp = self._d[x]
            self._d[x] = (cp - 1, vp)
            for i in range(1, self._log + 1):
                self._update(x >> i)

       

        
    
    def get(self, p):
        assert 0 <= p < self._n
        return self._d[p + self._size]

    def prod(self, l, r):
        assert 0 <= l <= r <= self._n
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    def all_prod(self):
        return self._d[1]

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

N, Q = map(int, readline().split())
As = list(map(int, readline().split()))

def op(x, y):
    cx, vx = x
    cy, vy = y
    if cx == 0 and cy == 0:
        return (0, min(vx, vy))
    elif cx == 0:
        return (0, vx)
    elif cy == 0:
        return (0, vy)
    else:
        return (1, 100)
    
def e():
    return (0, inf)
    
Ar = [(0, i) for i in range(0,  (2 * 10**5 ) + 2)]
for a in As:
    if a >= 0 and a <= (2 * 10**5) + 1:
        c, i = Ar[a]
        Ar[a] = (c+1, i)
st = SegTree(op, e, len(Ar), Ar)
for _ in range(Q):
    i, x = map(int, readline().split())
    st.set(x, As[i-1])
    As[i-1] = x
    print(st.all_prod()[1])