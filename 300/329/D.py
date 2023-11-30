import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 7
1 2 2 3 1 3 3
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
    
    def set(self, p):
        assert 0 <= p < self._n
        p += self._size
        self._d[p][0] += 1
        for i in range(1, self._log + 1):
            self._update(p >> i)
    
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

def op(x, y):
    xn, xi = x
    yn, yi = y
    if xn == yn:
        return xn, min(xi, yi)
    elif xn > yn:
        return xn, xi
    else:
        return yn, yi

def e():
    return -1, 0
    
N, M = map(int, readline().split())
v = [[0, i] for i in range(N)]
st = SegTree(op, e, N, v)
As = list(map(int, readline().split()))
for a in As:
    st.set(a-1)
    print(st.prod(0, N)[1] + 1)