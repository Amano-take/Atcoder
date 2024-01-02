import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
class UnionFind:
    def __init__(self, n, weight=False):
        self.n = n
        self.parents = [-1] * n
        self.is_weight = weight
        if weight:
            # 親との差
            self.diff_parent = [0] * n

    def find_with_weight(self, x):
        if self.parents[x] < 0:
            return x, 0
        else:
            parent, diff = self.find_with_weight(self.parents[x])
            self.parents[x] = parent
            self.diff_parent[x] += diff
            return self.parents[x], self.diff_parent[x]

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def diff(self, x, y):
        """
        return w_y - w_x
        """
        px, wx = self.find_with_weight(x)
        py, wy = self.find_with_weight(y)
        if px != py:
            raise ValueError("They belong to different groups.")
        else:
            return wy - wx

    def union_with_weight(self, x, y, w):
        """
        weight(y) = weight(x) + w
        """
        px, wx = self.find_with_weight(x)
        py, wy = self.find_with_weight(y)
        assert wx == self.diff_parent[x]
        assert wy == self.diff_parent[y]
        if px == py:
            # vx = w_px + wx, vy = w_px + wy, vy = vx + w
            # w_px = vx - wx -> vy = vx + wy - wx
            if wy - wx != w:
                raise ValueError("Weight mismatch!")
            else:
                return

        # pxのほうが常に大きいチームに変更->pxが融合後のチームリーダー（この方が高さが小さい）
        if self.parents[px] > self.parents[py]:
            px, py = py, px
            wx, wy = wy, wx
            w = -w
        
        self.parents[px] += self.parents[py]
        self.parents[py] = px
        # v_py = v_px + ???, w_y = w_x + w -> v_py + wy = v_px + wx + w
        self.diff_parent[py] = wx + w - wy


    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find_with_weight(x)[0] == self.find_with_weight(y)[0]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = ddict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())
    


    def copy(self):
        newuf = UnionFind(self.n, self.is_weight)
        newuf.parents = self.parents.copy()
        if self.is_weight:
            newuf.diff_parent = self.diff_parent.copy()
        return newuf
    
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
        if rx == ry:
            if self.diff(x, y) != w:
                raise ValueError("Weight mismatch!")
            else:
                return
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

sys.stdin = open("200/80/280/Fin.txt", "r")
file = open("200/80/280/Ftrueout.txt", "r")
writefile = open("200/80/280/Fout.txt", "w")

check = lambda x: print(x) if str(x) != file.readline().strip() else True
writef = lambda x: writefile.write(str(x) + "\n")
input=lambda: sys.stdin.readline().strip()

N, M, Q = map(int, input().split())


ufwithweight = UnionFind(N, True)
uf2 = WeightedUnionFind(N)
infinitset = set()
for i in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    try:
        ufwithweight.union_with_weight(u, v, w)
        uf2.union(u, v, w)
    except ValueError:
        infinitset.add(u)



infsetparent = set()

for i in infinitset:
    infsetparent.add(ufwithweight.find_with_weight(i)[0])


for i in range(Q):
    x, y = map(int, input().split())

    if ufwithweight.same(x-1, y-1):
        if ufwithweight.find_with_weight(x-1)[0] in infsetparent:
            check("inf")
            writef("inf")
        else:
            check(ufwithweight.diff(x-1, y-1))
            writef(ufwithweight.diff(x-1, y-1))
            #print(ufwithweight.diff(x-1, y-1))
            
    else:
        check("nan")
        writef("nan")