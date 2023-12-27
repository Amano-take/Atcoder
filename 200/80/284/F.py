import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
import random
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3
agccga
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
class RConst:
    Mask30 = (1 << 30) - 1
    Mask31 = (1 << 31) - 1
    Mod = (1 << 61) - 1
    cf = 0
    rui_cf = [1]

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
    
    @staticmethod
    def make_rui_cf(x: int):
        l = len(RConst.rui_cf)
        for _ in range(x - l + 1):
            RConst.rui_cf.append(RConst.mul(RConst.cf, RConst.rui_cf[-1]))

N = int(input())
S = input()
K = random.randint(1 << 31, RConst.Mod)
reverseK = pow(K, -1, RConst.Mod)
RConst.cf = K
RConst.make_rui_cf(N)
hash1 = 0
hash2 = 0
for i in range(N):
    hash1 += ord(S[i]) * RConst.rui_cf[i]

for i in range(N):
    hash2 += ord(S[2*N-1-i]) * RConst.rui_cf[i]

for i in range(N-1, -1, -1):
    if hash1 == hash2:
        print(S[:i+1] + S[N+1+i:])
        print(i+1)
        exit()
    
    hash1 = RConst.sub(hash1, ord(S[i])*RConst.rui_cf[i])
    hash1 = RConst.calc_mod(hash1 + ord(S[N+i]) * RConst.rui_cf[i])
    hash2 = RConst.sub(hash2, ord(S[N+i]))
    hash2 = RConst.mul(hash2, reverseK)
    hash2 = RConst.calc_mod(hash2 + ord(S[i]) * RConst.rui_cf[N-1])

print(-1)