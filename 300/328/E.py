from collections import defaultdict
import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)

from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    def init_copy(self, n, parents):
        self.n = n
        self.parents = parents.copy()

    def copy(self):
        uf2 = UnionFind(2)
        uf2.init_copy(self.n, self.parents)
        return uf2

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

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
8 28 936294041850197
1 2 473294720906780
1 3 743030800139244
1 4 709363019414774
1 5 383643612490312
1 6 557102781022861
1 7 623179288538138
1 8 739618599410809
2 3 857687812294404
2 4 893923168139714
2 5 581822471860662
2 6 740549363586558
2 7 307226438833222
2 8 447399029952998
3 4 636318083622768
3 5 44548707643622
3 6 307262781240755
3 7 12070267388230
3 8 700247263184082
4 5 560567890325333
4 6 704726113717147
4 7 588263818615687
4 8 549007536393172
5 6 779230871080408
5 7 825982583786498
5 8 713928998174272
6 7 751331074538826
6 8 449873635430228
7 8 11298381761479
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N, M, K = map(int, readline().split())
graph = defaultdict(list)
dp = [[] for _ in range(M+1)]
dp[0].append((UnionFind(N), 0))
for i in range(M):
    u, v, w = map(int, readline().split())
    u, v = u-1, v-1
    w %= K
    for uf, cost in dp[i]:
        dp[i+1].append((uf.copy(), cost))
        if not uf.same(u, v):
            uf.union(u, v)
            dp[i+1].append((uf.copy(), (cost+w) % K))
ans = inf

for uf, cost in dp[-1]:
    if uf.group_count() == 1:
        ans = min(ans, cost)
print(ans)