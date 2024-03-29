import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product, permutations
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3
1 10 100
10 1 100
100 10 1
1
1 2
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N = int(input())
Times = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
ng = ddict(set)
for _ in range(M):
    a, b = map(int, input().split())
    ng[a].add(b)
    ng[b].add(a)

def permutation_rec(perm, rest):

    if len(rest) == 0:
        return [perm]
    result = []
    for i in range(len(rest)):
        if len(perm) == 0 or rest[i] not in ng[perm[-1]]:
            result.extend(permutation_rec(perm + [rest[i]], rest[:i] + rest[i+1:]))
    return result

ans = inf
for perm in permutation_rec([], list(range(1, N+1))):
    time = 0
    for i in range(N):
        time += Times[perm[i]-1][i]
    ans = min(ans, time)
print(ans if ans != inf else -1)
