import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
4
15 5 2 10
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
pe = list(map(int, input().split()))
a = pe[0]
ans = 0
for i in range(1, N):
    ans = max(ans, pe[i] - a + 1)
print(ans)