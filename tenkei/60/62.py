import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
6
5 5
2 4
6 6
5 2
1 3
4 1
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()

white = set()
que = deque()
ans = deque()
N = int(input())
graph = ddict(set)
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if  a == i or b == i:
        white.add(i)
        que.append(i)
        ans.append(i)
    else:
        graph[a].add(i)
        graph[b].add(i)
while que:
    v = que.popleft()
    for u in graph[v]:
        if u in white:
            continue
        white.add(u)
        que.append(u)
        ans.append(u)

if len(white) == N:
    while ans:
        print(ans.pop() + 1)
else:
    print(-1)
