import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
A C
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
dis = [3, 1, 4, 1, 5, 9]
p, q = input().split()
ip, iq = ord(p) - ord("A"), ord(q) - ord("A")
ip, iq = min(ip, iq), max(ip, iq)
ans = 0
for i in range(ip, iq):
    ans += dis[i]
print(ans)