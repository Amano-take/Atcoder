import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
AAAAAAAAAA
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
S = list(readline().strip())
reverseS = list(reversed(S))
ans = 0
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        if (S[i:j]) == reverseS[len(S)-j:len(S)-i]:
            ans = max(ans, j-i)
print(ans)
