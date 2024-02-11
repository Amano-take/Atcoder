import sys, io
import math, heapq, bisect
from collections import deque, defaultdict as ddict
from itertools import product
inf = float("inf")
sys.setrecursionlimit(10**8)
_INPUT = """\
-2 0
"""
sys.stdin = io.StringIO(_INPUT)
input=lambda: sys.stdin.readline().strip()
A, B = map(int, input().split())
if A == 0:
    if B == 2 or B == -2:
        print(1, 0)
    elif B == 1 or B == -1:
        print(2, 0)
    else:
        print(-1)
    exit()
if B == 0:
    if A == 2 or A == -2:
        print(0, 1)
    elif A == 1 or A == -1:
        print(0, 2)
    else:
        print(-1)
    exit()

#search x, y s.t. Ay - Bx = 2 or -2
def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extgcd(b, a % b)
        return d, y, x - a // b * y
if A >= 0 and B >= 0:
    d, x, y = extgcd(B, A)
    if d == 1:
        ansx = -x * 2
        ansy = y * 2
        ansx2 = -ansx
        ansy2 = -ansy
    elif d == 2:
        ansx = -x
        ansy = y
        ansx2 = -ansx
        ansy2 = -ansy
    else:
        print("-1")
        exit()
elif A >= 0 and B < 0:
    d, x, y = extgcd(-B, A)
    if d == 1:
        ansx = -x * 2
        ansy = -y * 2
        ansx2 = -ansx
        ansy2 = -ansy
    elif d == 2:
        ansx = -x
        ansy = -y
        ansx2 = -ansx
        ansy2 = -ansy
    else:
        print("-1")
        exit()
elif A < 0 and B >= 0:
    d, x, y = extgcd(B, -A)
    if d == 1:
        ansx = x * 2
        ansy = y * 2
        ansx2 = -ansx
        ansy2 = -ansy
    elif d == 2:
        ansx = x
        ansy = y
        ansx2 = -ansx
        ansy2 = -ansy
    else:
        print("-1")
        exit()
else:
    d, x, y = extgcd(-B, -A)
    if d == 1:
        ansx = x * 2
        ansy = -y * 2
        ansx2 = -ansx
        ansy2 = -ansy
    elif d == 2:
        ansx = x
        ansy = -y
        ansx2 = -ansx
        ansy2 = -ansy
    else:
        print("-1")
        exit()
def ceil_div(x, y):
    if x % y == 0:
        return x // y
    else:
        return x // y + 1
def floor_div(x, y):
    if x % y == 0:
        return x // y
    else:
        return x // y
    
def make_ans(x, y, A, B):
    if x > -10**17 and x < 10**17 and y > -10**17 and y < 10**17:
        return x, y
    if A > 0:
        xkmin = ceil_div(-10**17 - x, A)
        xkmax = floor_div(10**17 - x, A)
    else:
        xkmin = ceil_div(10**17 - x, -A)
        xkmax = floor_div(-10**17 - x, -A)
    if B > 0:
        ykmin = ceil_div(-10**17 - y, B)
        ykmax = floor_div(10**17 - y, B)
    else:
        ykmin = ceil_div(10**17 - y, -B)
        ykmax = floor_div(-10**17 - y, -B)

    start = max(xkmin, ykmin)
    end = min(xkmax, ykmax)
    if int(start) == start and start <= end:
        return x + start * A, y + start * B
    elif int(start) + 1 <= end:
        return x + (int(start) + 1) * A, y + (int(start) + 1) * B
    else:
        return -1
    
if make_ans(ansx, ansy, A, B) != -1:
    print(*make_ans(ansx, ansy, A, B))
    exit()
elif make_ans(ansx2, ansy2, A, B) != -1:
    print(*make_ans(ansx2, ansy2, A, B))
    exit()
else:
    print("-1")

