import sys
import io
import math
from collections import defaultdict
sys.setrecursionlimit(10**8)
_INPUT = """\
5 7
1 2 0 0
1 2 0 0
2 3 0 0
3 1 0 0
2 1 0 0
3 2 0 0
4 5 0 0
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

N, M = map(int, readline().split())
graph = defaultdict(set)
pos = defaultdict(tuple)
for _ in range(M):
    A, B, X, Y = map(int, readline().split())
    graph[A].add(B)
    graph[B].add(A)
    pos[(A, B)] = (X, Y)
    pos[(B, A)] = (-X, -Y)
ans = [[] for _ in range(N)]
ans[0] = [0, 0]

def dfs(node, visit:set):
    for child in graph[node]:
        if child in visit:
            continue
        else:
            if len(ans[child-1]) == 0:
                ans[child-1] = [ans[node-1][0] + pos[(node, child)][0], ans[node-1][1] + pos[(node, child)][1]]
                visit.add(child)
                dfs(child, visit)
                visit.remove(child)

dfs(1, set([1]))
for a in ans:
    if len(a) == 0:
        print("undecidable")
    else:
        print(*a)