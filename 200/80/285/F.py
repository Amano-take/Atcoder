import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6
abcdcf
4
2 1 3
2 2 6
1 5 e
2 2 6
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

N = int(input())
S = list(input())

def e():
    return [[0] * 26, True]

def op(a, b):
    sa, fa = a
    sb, fb = b
    maxa  = 0
    minb = 27
    for i in range(26):
        if sa[i] != 0:
            maxa = i
        if sb[i] != 0 and minb == 27:
            minb = i
    
    return [[sa[i] + sb[i] for i in range(26)], fa and fb and maxa <= minb]

v = [[[0] * 26, True] for _ in range(N)]
for i in range(N):
    v[i][0][ord(S[i]) - ord('a')] = 1


st = SegTree(op, e, N, v)

def substring(all, sub):
    minsub = -1
    maxsub = 0
    for i in range(26):
        if sub[i] != 0 and minsub == -1:
            minsub = i
        if sub[i] != 0:
            maxsub = i
    for i in range(minsub, maxsub+1):
        if i == minsub or i == maxsub:
            if all[i] < sub[i]:
                return False
        else:
            if all[i] != sub[i]:
                return False
    return True

Q = int(input())
for _ in range(Q):
    q, a, b = input().split()
    if q == '1':
        st.set(int(a)-1, [[1 if i == ord(b) - ord('a') else 0 for i in range(26)], True])
    else:
        q = st.prod(int(a)-1, int(b))
        
        all = st.prod(0, N)
        if q[1] and substring(all[0], q[0]):
            print('Yes')
        else:
            print('No') 
