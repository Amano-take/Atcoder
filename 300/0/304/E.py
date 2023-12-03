import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
6 6
1 2
2 3
2 3
3 1
5 4
5 5
3
1 5
2 6
4 3
4
2 5
2 6
5 6
5 4
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

from collections import defaultdict

class UnionFind():
    def __init__(self, n, weight=False):
        self.n = n
        self.parents = [-1] * n
        self.is_weight = weight
        if weight:
            #親との差
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
        if px == py:
            #vx = w_px + wx, vy = w_px + wy, vy = vx + w
            #w_px = vx - wx -> vy = vx + wy - wx
            if wy - wx != w:
                raise ValueError("Weight mismatch!")
            else:
                return
        
        #pxのほうが常に大きいチームに変更->pxが融合後のチームリーダー（この方が高さが小さい）
        if self.parents[px] > self.parents[py]:
            px, py = py, px
            wx, wy = wy, wx
            w = -w

        self.parents[px] += self.parents[py]
        self.parents[py] = px
        #v_py = v_px + ???, w_y = w_x + w -> v_py + wy = v_px + wx + w
        self.diff_parent[py] = wx + w - wy

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)
    

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    
    def copy(self):
        newuf = UnionFind(self.n, self.is_weight)
        newuf.parents = self.parents.copy()
        if self.is_weight:
            newuf.diff_parent = self.diff_parent.copy()
        return newuf
    
N, M = map(int, readline().split())
uf = UnionFind(N)
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, readline().split())
    uf.union(u, v)
K = int(input())
setXY = set()

for _ in range(K):
    x, y = map(lambda x: int(x) - 1, readline().split())
    px = uf.find(x)
    py = uf.find(y)
    setXY.add((px, py))

Q = int(input())
for _ in range(Q):
    p, q = map(lambda x: int(x) - 1, readline().split())
    pp = uf.find(p)
    pq = uf.find(q)
    if (pp, pq) in setXY or (pq, pp) in setXY:
        print("No")
    else:
        print("Yes")