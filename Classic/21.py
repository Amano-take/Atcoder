import sys
import io
from collections import defaultdict as ddict
sys.setrecursionlimit(10**8)
_INPUT="""\
4 7
1 2
2 1
2 3
4 3
4 1
1 4
2 3
"""
sys.stdin=io.StringIO(_INPUT)
readline = sys.stdin.readline
N, M = map(int, readline().split())
reachable = ddict(set)
can_go = ddict(set)
for i in range(1, N+1):
    reachable[i].add(i)
    can_go[i].add(i)
for _ in range(M):
    A, B = map(int, readline().split())
    reachable[B] |= (reachable[A])
    can_go[A] |= can_go[B]
ans = 0
for i in range(1, N+1):
    ans += len(reachable[i].intersection(can_go[i])) - 1
    print(reachable[i].intersection(can_go[i]))


print(reachable)
print(can_go)


