import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product, combinations, permutations
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 4
1 2 5
2 1 -3
2 3 -4
3 1 100
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
# -----------------------------
n, m = map(int, input().split())

dp = [[inf]* (n * (n-1) // 2) for _ in range(1 << n)]
combis = list(combinations(range(n), 2))
index_combis = ddict(int)
for i, combi in enumerate(combis):
    index_combis[combi] = i
    a, b = combi
    index_combis[(b, a)] = i

bitcount = ddict(list)
for i in range(1 << n):
    bitcount[bin(i).count("1")].append(i)

graph = ddict(set)
weight = ddict(lambda: inf)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)
    a, b = min(a, b), max(a, b)
    weight[(a-1, b-1)] = min(weight[(a-1, b-1)], c)

for a, b in combis:
    alpha, beta = min(a, b), max(a, b)
    if weight[(alpha, beta)] != inf:
        dp[1 << alpha | 1 << beta][index_combis[(alpha, beta)]] = weight[(alpha, beta)]

for s in range(2, n):
    for bit in bitcount[s]:
        for index, (a, b) in enumerate(combis):
            for u in graph[a]:
                if (bit >> u) & 1 == 0:
                    dp[bit | 1 << u][index_combis[(u, b)]] = min(dp[bit | 1 << u][index_combis[(u, b)]], dp[bit][index] + weight[(u, b)])
            for u in graph[b]:
                if (bit >> u) & 1 == 0:
                    dp[bit | 1 << u][index_combis[(a, u)]] = min(dp[bit | 1 << u][index_combis[(a, u)]], dp[bit][index] + weight[(a, u)])

print(dp)
print(combis)
print(min(dp[-1]) if min(dp[-1]) != inf else "No")



    

