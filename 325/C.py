import sys
import io
import math
from collections import defaultdict
sys.setrecursionlimit(10**8)
_INPUT = """\
5 6
.##...
...#..
....##
#.#...
..#...
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
H, W = map(int, readline().split())



class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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
    
sensors = defaultdict(int)
sensormap = []
index = 0
for i in range(H):
    l = list(input().strip())
    sensormap.append(l)
    for j, x in enumerate(l):
        if x == "#":
            sensors[(i, j)] = index
            index += 1

ans = 0
uf = UnionFind(len(sensors))
for (y, x), index in sensors.items():
    cand = [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
    for cx, cy in cand:
        if cx < 0 or cx >= W or cy < 0 or cy >= H:
            continue
        else:
            if sensormap[cy][cx] == "#":
                uf.union(index, sensors[(cy, cx)])
print(uf.group_count())