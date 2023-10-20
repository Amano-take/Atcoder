import sys
import io
import math
from collections import defaultdict as ddict, deque
sys.setrecursionlimit(10**8)
_INPUT = """\
3 4 6
1 2
2 3
4 5
4 6
1 3
6 7
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N1, N2, M = map(int, readline().split())
graphN1 = ddict(set)
graphN2 = ddict(set)

for _ in range(M):
    a, b = map(int, readline().split())
    if a <= N1:
        graphN1[a].add(b)
        graphN1[b].add(a)
    else:
        graphN2[a].add(b)
        graphN2[b].add(a)

def dfs(graph:ddict, start):
    queue = deque()
    queue.append(start)
    havebeen = set()
    havebeen.add(start)
    ans = [-1] * (N1 + N2 + 1)
    ans[start] = 0
    while len(queue) != 0:
        s = queue.popleft()
        for next in graph[s]:
            if next not in havebeen:
                ans[next] = ans[s] + 1
                queue.append(next)
                havebeen.add(next)
    return ans

print(max(dfs(graphN1, 1)) + max(dfs(graphN2, N1+N2)) + 1)

