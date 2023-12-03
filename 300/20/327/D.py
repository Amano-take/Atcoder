import sys
import io
import math
from collections import defaultdict as ddict, deque
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
3 2
1 2
2 3
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N, M = map(int, readline().split())
As = list(map(lambda x: int(x) - 1, readline().split()))
Bs = list(map(lambda x: int(x) - 1, readline().split()))
graph = ddict(set)
for i in range(M):
    graph[As[i]].add(Bs[i])
    graph[Bs[i]].add(As[i])
color = [-1] * N
stack = deque([0])
def coloring(p, ss):
    stack = deque([p])
    while len(stack) != 0:
        node = stack.pop()
        for next in graph[node]:
            if color[next] != -1 and color[node] == color[next]:
                break
            elif color[next] == -1:
                color[next] = int(not(color[node]))
                ss.remove(next)
                stack.append(next)
        else:
            continue
        print("No")
        exit()
    return ss

ss = set(range(N))
while len(ss) != 0:
    p = ss.pop()
    color[p] = 0
    ss = coloring(p, ss)
print("Yes")
