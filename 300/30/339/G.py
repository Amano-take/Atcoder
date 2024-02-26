import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
8
2 0 2 4 0 2 0 3
5
1 8 3
10 12 11
3 3 2
3 6 5
12 0 11
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

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
        assert 0 <= p < self._n
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)
    
    def get(self, p):
        assert 0 <= p < self._n
        return self._d[p + self._size]

    def prod(self, l, r, op2, D):
        assert 0 <= l <= r <= self._n
        ans = 0
        l += self._size
        r += self._size
        op = op2

        while l < r:
            if l & 1:
                ans += op(self._d[l], D)
                l += 1
            if r & 1:
                r -= 1
                ans += op(self._d[r], D)
            l >>= 1
            r >>= 1
        return ans
    
    def all_prod(self):
        return self._d[1]

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

def op(x, y):
    cumsum0, li0 = x
    cumsum1, li1 = y
    li = []
    i = j = 0
    while i < len(li0) and j < len(li1):
        if li0[i] < li1[j]:
            li.append(li0[i])
            i += 1
        else:
            li.append(li1[j])
            j += 1
    while i < len(li0):
        li.append(li0[i])
        i += 1
    while j < len(li1):
        li.append(li1[j])
        j += 1
    cumsum = [0]
    for i in range(len(li)):
        cumsum.append(cumsum[-1] + li[i])
    return (cumsum, li)

def op2(x, D):
    cumsum0, li0 = x
    t0 = bisect.bisect_right(li0, D)
    return cumsum0[t0]
N = int(input())
As = list(map(int, input().split()))
def make(x):
    return [0, x], [x]
st = SegTree(op, lambda: ([0], []), N, list(map(make, As)))
Q = int(input())
key = 0
for _ in range(Q):
    a, b, c = map(lambda x: int(x) ^ key, input().split())
    a -= 1
    b -= 1
    key = st.prod(a, b + 1, op2, c)
    print(key)    