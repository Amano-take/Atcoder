import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
6 6
1 6
6 5
6 2
2 3
4 3
4 2
"""
sys.stdin = io.StringIO(_INPUT)
N, M = map(int, input().split())
kouho = set(range(N))
for _ in range(M):
    a, b = (map(lambda x: int(x) - 1, input().split()))
    if b in kouho:
        kouho.remove(b)

if len(kouho) == 1:
    print(kouho.pop() + 1)
else:
    print(-1)