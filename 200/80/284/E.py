import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
import time
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
4 6
1 2
1 3
1 4
2 3
2 4
3 4
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
Graph = ddict(list)
for _ in range(M):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)

#dfs count path
ans = 0
def dfs(start, visited):
    global ans
    ans += 1
    if ans == 10**6:
        print(10**6)
        exit()
    visited[start] = True
    for next in Graph[start]:
        if visited[next] == False:
            dfs(next, visited)
            visited[next] = False
    return ans

visited = [False] * (N+1)
print(dfs(1, visited))