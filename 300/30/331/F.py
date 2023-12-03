import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
import random

inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
7 8
abcbacb
2 1 5
2 4 7
2 2 2
1 5 c
2 1 5
2 4 7
1 4 c
2 3 6
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()


class RConst:
    Mask30 = (1 << 30) - 1
    Mask31 = (1 << 31) - 1
    Mod = (1 << 61) - 1

    @staticmethod
    def calc_mod(x: int) -> int:
        xu, xd = x >> 61, x & RConst.Mod
        ret = xu + xd
        if RConst.Mod <= ret:
            ret -= RConst.Mod
        return ret

    @staticmethod
    def sub(a: int, b: int) -> int:
        if a < b:
            return a + RConst.Mod - b
        return a - b

    @staticmethod
    def mul(a: int, b: int) -> int:
        au, ad = a >> 31, a & RConst.Mask31
        bu, bd = b >> 31, b & RConst.Mask31
        mid = ad * bu + au * bd
        midu, midd = mid >> 30, mid & RConst.Mask30
        return RConst.calc_mod(((au * bu) << 1) + midu + (midd << 31) + ad * bd)



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
cf1 = random.randrange(1<<31, RConst.Mod)
cf2 = random.randrange(1<<31, RConst.Mod)
cf_table1 = [1]
cf_table2 = [1]
N, Q = map(int, input().split())
for _ in range(N):
    cf_table1.append(RConst.mul(cf_table1[-1], cf1))
    cf_table2.append(RConst.mul(cf_table2[-1], cf2))


def op1(x, y):
    lenx, hashx, rhashx = x
    leny, hashy, rhashy = y
    return lenx + leny, RConst.calc_mod( RConst.mul(cf_table1[leny], hashx) + hashy), RConst.calc_mod(RConst.mul(cf_table1[lenx], rhashy) + rhashx)

def op2(x, y):
    lenx, hashx, rhashx = x
    leny, hashy, rhashy = y
    return lenx + leny, RConst.calc_mod( RConst.mul(cf_table2[leny], hashx) + hashy), RConst.calc_mod(RConst.mul(cf_table2[lenx], rhashy) + rhashx)

def hash1(s):
    return 1, ord(s), ord(s)

def e():
    return (0, 0, 0)
S = list(input())
v = list(map(hash1, S))
st1 = SegTree(op1, e, N, v)
st2 = SegTree(op2, e, N, v)
for _ in range(Q):
    var, x, y = input().split()
    if var == "1":
        x = int(x)
        st1.set(x-1, hash1(y))
        st2.set(x-1, hash1(y))
    else:
        x = int(x) -1
        y = int(y)
        _, h, rh = st1.prod(x, y)
        _, h2, rh2 = st2.prod(x, y)
        if h == rh and h2 == rh2:
            print("Yes")
        else:
            print("No")