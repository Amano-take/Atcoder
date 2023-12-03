import sys
import io
import math
from collections import defaultdict as ddict, deque
sys.setrecursionlimit(10**8)
_INPUT = """\
9
3 9
7 8
8 6
4 6
4 1
5 9
7 3
5 2
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
graph = ddict(list)
for _ in range(N-1):
    s, g = map(int, readline().split())
    graph[s].append(g)
    graph[g].append(s)

for i, li in graph.items():
    if len(li) == 1:
        start = i
        break

stack = deque([start])
star = set()
edge = set([start])
while len(stack) > 0:
    p = stack.pop()
    if p in edge:
        #多くても二つ
        nexts = graph[p]
        if len(nexts) == 1:
            next = nexts[0]
            if next not in star:
                star.add(next)
                stack.append(next)
        else:
            a, b = nexts
            if a in star:
                stack.append(b)
                edge.add(b)
            elif a in edge:
                stack.append(b)
                star.add(b)
            elif b in star:
                stack.append(a)
                edge.add(a)
            else:
                stack.append(a)
                star.add(a)

    elif p in star:
        for next in graph[p]:
            if next not in edge:
                edge.add(next)
                stack.append(next)

ans = []
for c in star:
    ans.append(len(graph[c]))
ans.sort()
print(*ans)
