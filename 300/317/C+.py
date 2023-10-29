import sys
import io
from collections import defaultdict
sys.setrecursionlimit(10**8)

readline = sys.stdin.readline
N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

ans = 0

def dfs(s, exs, cost):
    global ans
    if cost > ans:
        ans = cost
    
    for next, length in graph[s]:
        if next not in exs:
            exs.add(s)
            dfs(next, exs, cost+length)
            exs.remove(s)

for i in range(1, N+1):
    dfs(i, set(), 0)

print(ans)