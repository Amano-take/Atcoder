from collections import deque
import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
7 3
1 2 1 3 3 3
1 1
1 2
4 3
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N, M = map(int, readline().split())
parents = list(map(int, readline().split()))
tree = [[] for _ in range(N)]
for i, p in enumerate(parents):
    i += 1
    tree[p-1].append(i)
insurance = [-1] * N
for _ in range(M):
    a, b = map(int, readline().split())
    insurance[a-1] = max(insurance[a-1], b)

ans = 0
stack = deque([0])
while len(stack) != 0:
    p = stack.pop()
    ins = insurance[p]
    if ins >= 0:
        ans += 1
    for c in tree[p]:
        insurance[c] = max(insurance[c], ins-1)
        stack.append(c)
print(ans)