import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
3
5 0
3 3
2 18
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
wx = []
for _ in range(N):
    wx.append(list(map(int, readline().split())))
ans = 0
for i in range(24):
    #i~i+1
    temp = 0
    for w, x in wx:
        start = (x + i) % 24
        if start >= 9 and start <= 17:
            temp += w
    ans = max(ans, temp)
print(ans)