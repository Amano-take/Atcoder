import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
125 175 250 300 400 525 600 650
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
S = list(map(int, readline().split()))
for i in range(len(S)):
    s = S[i]
    if s % 25 != 0:
        break
    if s < 100 or s > 675:
        break
    if i != 0 and s < S[i-1]:
        
        break
else:
    print("Yes")
    exit()
print("No")