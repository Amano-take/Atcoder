import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
from collections import defaultdict

class UnionFind():
    def __init__(self, n, weight=False):
        self.n = n
        self.parents = [-1] * n
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
    

_INPUT = """\
5 20
4 2 125421359
2 5 -191096267
3 4 -42422908
3 5 -180492387
3 3 174861038
2 3 -82998451
3 4 -134761089
3 1 -57159320
5 2 191096267
2 4 -120557647
4 2 125421359
2 3 142216401
4 5 -96172984
3 5 -108097816
1 5 -50938496
1 2 140157771
5 4 65674908
4 3 35196193
4 4 0
3 4 188711840
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()

N, Q = map(int, readline().split())
uf = UnionFind(N, True)
ans = []
for i in range(Q):
    a, b, d = map(int, readline().split())
    a -= 1
    b -= 1
    try:

        uf.union_with_weight(b, a, d)
        ans.append(i+1)
    except:
        continue
print(" ".join(map(str, ans)))
