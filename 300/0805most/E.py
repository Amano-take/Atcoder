import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
9
123456789
"""
sys.stdin = io.StringIO(_INPUT)
ANSDIV = 998244353
N = int(input())
S = input()
flag = True
for i in range(N -1):
    if S[i] != str(1) and S[i+1] != str(1):
        print(-1)
        flag = False
        break
        
ans = 0
S = S[1:]
if flag:
    for s in reversed(S):
        ans += ans*(int(s) -1) + int(s)
        ans %= ANSDIV
    print(ans)
