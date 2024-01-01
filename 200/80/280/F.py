import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)

class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        # 根への距離を管理
        self.weight = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    # 併合
    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    # 同じ集合に属するか
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

_INPUT = """\
9 7 5
3 1 4
1 5 9
2 6 5
1 5 8
9 7 9
3 2 3
8 4 6
2 6
4 3
3 8
3 2
7 9
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

N, M, Q = map(int, input().split())


ufwithweight = WeightedUnionFind(N)
infinitset = set()
for i in range(M):
    u, v, w = map(int, input().split())
    if ufwithweight.same(u-1, v-1):
        if ufwithweight.diff(u-1, v-1) != w:
            infinitset.add(u-1)
    else:
        ufwithweight.union(u-1, v-1, w)


infsetparent = set()

for i in infinitset:
    infsetparent.add(ufwithweight.find(i))


for i in range(Q):
    x, y = map(int, input().split())
    if ufwithweight.same(x-1, y-1):
        if ufwithweight.find(x-1) in infsetparent:
            print("inf")
        else:
            print(ufwithweight.diff(x-1, y-1))
    else:
        print("nan")