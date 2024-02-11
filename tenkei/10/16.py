import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
9999
1 5 10
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
A.sort()
A, B, C = A
ans = 10 ** 5
rest = N - C * (N // C) - C
for c in range(N // C, -1, -1):
    rest += C
    if rest == 0:
        ans = c
        break
    if rest // B + c > ans:
        break
    
    res = rest - (rest // B) * B - B
    for b in range(rest // B, -1, -1):
        res += B
        if res == 0:
            ans = min(ans, b + c)
            break
        if res // A + b + c> ans:
            break
        if res % A == 0:
            ans = min(ans, b + c + res // A)

        
print(ans)
