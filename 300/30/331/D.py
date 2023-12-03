import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 2
WWB
BBW
WBW
1 2 3 4
0 3 4 5
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, Q = map(int, input().split())
Ps = [list(input()) for _ in range(N)]

L = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if Ps[i][j] == "B":
            L[i][j] = 1

class Acc2:
    def __init__(self,l,f,unit,inv):
        self.h,self.w=len(l),len(l[0])
        self.acc2=[[unit]*(self.w+1) for _ in range(self.h+1)]
        self.f,self.inv=f,inv
        for i in range(self.h):
            for j in range(self.w):
                self.acc2[i+1][j+1]=f(f(f(self.acc2[i][j+1],self.acc2[i+1][j]),inv(self.acc2[i][j])),l[i][j])
    def sum(self,i,j,i_,j_):
        return self.f(self.f(self.f(self.acc2[i_][j_],self.inv(self.acc2[i][j_])),self.inv(self.acc2[i_][j])),self.acc2[i][j])
    def get(self,i,j):
        return self.sum(i,j,i+1,j+1)
    def __str__(self):
        return '\n'.join([str(i) for i in self.acc2])

###### Settings ######
_f=lambda x,y: x+y
_unit=0
_inv=lambda x: -x
######################


acc = Acc2(L, _f, _unit, _inv).acc2

for _ in range(Q):
    A, B, C, D = map(int, input().split())
    t = A // N
    l = B // N
    C += 1
    D += 1
    if C % N == 0:
        b = C // N
    else:
        b = C // N + 1
    
    if D % N == 0:
        r = D // N
    else:
        r = D // N + 1
    sum = acc[-1][-1] * (r - l) * (b - t)
    x = A - t * N
    y = B - l * N
    sum += acc[x][y] - acc[x][-1] * (r - l)
    p = b * N - C
    q = r * N - D
    sum += acc[x][-1] - acc[x][N-q] - (acc[-1][-1] - acc[-1][N - q]) * (b -t)
    sum += acc[-1][-1] + acc[N-p][N-q]  - acc[N-p][-1] - acc[-1][N-q] - (acc[-1][-1] - acc[N-p][-1]) * (r - l)
    sum += acc[-1][y] - acc[N-p][y] - (acc[-1][y]) * (b - t)
    print(sum)
