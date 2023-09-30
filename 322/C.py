import sys
import io
import bisect

sys.setrecursionlimit(10**8)
_INPUT = """\
8 5
1 3 4 7 8
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline

N, M = map(int, readline().split())
A = list(map(int, readline().split()))
setA = set(map(lambda x: x+1, A))
next = A[0]
for i in range(1, N+1):
    if i in setA:
        t = bisect.bisect_left(A, i)
        next = A[t]
    print(next - i)
