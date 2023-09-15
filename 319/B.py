import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
L = []
N = int(input())

for i in range(1, 10):
    if N % i == 0:
        L.append((i, N // i))

ans = []

for i in range(0, N+1):
    for k, xx in L:
        if i % xx == 0:
            ans.append(str(k))
            break
    else:
        ans.append("-")

print("".join(ans))
    
