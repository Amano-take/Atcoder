import sys
import io
sys.setrecursionlimit(10**8)
from collections import defaultdict
from collections import deque

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
_INPUT = """\
5
1 2
4 3
5 3
1 4
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
uf = UnionFind(N)
teamTree = [0] * (2*N-1)
teamTreeGraph = [0] * (2*N - 1)
memberRoot = [i for i in range(N)]



for i in range(N -1):
    index = N+i
    x, y = map(lambda x: int(x) - 1, input().split())
    mem_x, mem_y = uf.size(x), uf.size(y)
    root_x, root_y = uf.find(x), uf.find(y)
    teamTreeGraph[index] = (memberRoot[root_x], memberRoot[root_y])
    teamTree[index] = (mem_x, mem_y)
    uf.union(x, y)
    memberRoot[uf.find(x)] = index


MOD = 998244353
inv_mod = [0] * (N+1)
for i in range(1, N+1):
    inv_mod[i] = pow(i, -1, MOD)

answer = [0] * (2*N - 1)
stack = deque([2*N - 2])
while len(stack) != 0:

    index = stack.popleft()
    if index < N:
        continue
    ans = answer[index]

    left, right = teamTreeGraph[index]
    mem_left, mem_right = teamTree[index]

    answer[left] = (ans + mem_left * inv_mod[mem_left+mem_right] )% MOD
    answer[right] = (ans + mem_right * inv_mod[mem_left+mem_right]) % MOD
    stack.appendleft(left)
    stack.appendleft(right)

print(*answer[0:N])