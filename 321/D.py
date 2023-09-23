import sys
import io
import bisect
sys.setrecursionlimit(10**8)
_INPUT = """\
2 2 7
3 5
6 1
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline

N, M, P = map(int, readline().split())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
B.sort()
ruiseki = [0] * (len(B)+1)
ans = 0
for i in range(1, len(B)+1):
    ruiseki[i] = ruiseki[i-1] + B[i-1]
for a in A:
    index = bisect.bisect_left(B, P-a)
    ans += a * (index)
    ans += ruiseki[index]
    ans += P * (len(B) - index)
print(ans)