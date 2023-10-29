import sys
import io
import math
from collections import defaultdict as ddict
sys.setrecursionlimit(10**8)
_INPUT = """\
8
1 5
1 6
1 7
1 8
0
0
0
0
"""
sys.stdin = io.StringIO(_INPUT)
input = sys.stdin.readline
G = ddict(set)
N = int(input())
for i in range(N):
    C, *L = map(int, input().split())
    L = map(lambda x: x-1, L)
    G[i] = set(L)
used = [0] * N
ans = []

def dfs(node):
    used[node] = 1
    for suc in G[node]:
        if not used[suc]:
            dfs(suc)
    ans.append(node)

dfs(0)
ans.pop()

print(*list(map(lambda x: x+1, ans)))

