import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
7 6
5 R 3 R
7 R 4 R
4 B 1 R
2 R 3 B
2 B 5 B
1 B 7 B
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
graph = ddict(list)
for _ in range(M):
    p, sp, q, sq = input().split()
    p, q = map(int, [p, q])
    if sp == "R":
        p = p * 2 - 1
    else:
        p = p * 2
    
    if sq == "R":
        q = q * 2 - 1
    else:
        q = q * 2

    graph[p].append(q)
    graph[q].append(p)

for i in range(1, N+1):
    graph[i*2-1].append(i*2)
    graph[i*2].append(i*2-1)


#dfs with stack and find cycle
visited = [False] * (N*2+1)
stack = deque()
ans1 = 0
ans2 = 0
for i in range(1, N*2+1):
    if visited[i]:
        continue
    stack.append(i)
    while stack:
        v = stack.pop()
        if visited[v]:
            continue
        visited[v] = True
        for u in graph[v]:
            if visited[u]:
                continue
            stack.append(u)
    else:
        if abs(v -i) != 1 and i in graph[v]:
            ans1 += 1
        elif graph[v].count(i) == 2:
            ans1 +=1
        else:
            ans2 += 1
print(ans1, ans2)


