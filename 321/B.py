import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
3 100
100 100
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N, X = map(int, readline().split())
A = list(map(int, readline().split()))
A.sort()
min = A[0]
max = A[-1]
s = sum(A[1:N-2])
s_a = sum(A[1:N-1])
s_b = sum(A[0:N-2])
if X > s_a:
    print(-1)
elif X >= s_b:
    print(0)
elif X == s_a:
    print(max)
else:
    print(X-s)