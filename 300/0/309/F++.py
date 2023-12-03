import sys
inf = float('inf')
input = lambda: sys.stdin.readline().strip()
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))
MOD = 10**9+7
from collections import defaultdict

class BIT:
    def __init__(self, n):
        self.tree = [inf] * n
        self.n = n

    def update(self, i, mn):
        while i < self.n:
            self.tree[i] = min(self.tree[i], mn)
            i += i & -i

    def query(self, i):
        res = inf
        while i > 0:
            res = min(self.tree[i], res)
            i -= i & -i
        return res

def solve():
    n = II()
    s = set()
    d = defaultdict(list)
    for _ in range(n):
        x, y, z = sorted(MII())
        d[x].append((y, z))
        s.add(y)

    mp = {x: i + 1 for i, x in enumerate(sorted(s))}
    t = BIT(n + 1)
    for x in sorted(d.keys()):
        for y, z in d[x]:
            if t.query(mp[y] - 1) < z:
                return print('Yes')
        for y, z in d[x]:
            t.update(mp[y], z)
    print('No')
    return

solve()
