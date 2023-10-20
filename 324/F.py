import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
1 2 3 3 0 5
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
def move_min(sx, sy, gx, gy):
    return abs(gx - sx) + abs(gy - sy)

def move_min_jama(sx, sy, gx, gy, jx, jy):
    if sx == jx and sx == gx and (jy - sy) * (jy - gy) < 0:
        return abs(gx - sx) + abs(gy - sy) + 2
    elif sy == jy and sy == gy and (jx - sx) * (jx - gx) < 0:
        return abs(gx - sx) + abs(gy - sy) + 2
    else:
        return abs(gx - sx) + abs(gy - sy)

XA, YA, XB, YB, XC, YC = map(int, readline().split())
ans = 0
if XB == XC:
    if YB > YC:
        if XA == XB and YA < YB:
            ans += 2
        ans += move_min(XA, YA, XB, YB+1)
        ans += move_min(XB, YB, XC, YC)
    elif YC > YB:
        if XA == XB and YA > YB:
            ans += 2
        ans += move_min(XA, YA, XB, YB-1)
        ans += move_min(XB, YB, XC, YC)
elif XB > XC:
    if YB > YC:
        p1 = move_min_jama(XA, YA, XB+1, YB, XB, YB)
        p2 = move_min_jama(XA, YA, XB, YB+1, XB, YB)
        ans += min(p1, p2)
        ans += move_min(XB, YB, XC, YC)
        ans += 2
    elif YC > YB:
        p1 = move_min_jama(XA, YA, XB+1, YB, XB, YB)
        p2 = move_min_jama(XA, YA, XB, YB-1, XB, YB)
        ans += min(p1, p2)
        ans += move_min(XB, YB, XC, YC)
        ans += 2
    elif YC == YB:
        ans += move_min_jama(XA, YA, XB+1, YB, XB, YB)
        ans += move_min(XB, YB, XC, YC)
else:
    if YB > YC:
        p1 = move_min_jama(XA, YA, XB-1, YB, XB, YB)
        p2 = move_min_jama(XA, YA, XB, YB+1, XB, YB)
        ans += min(p1, p2)
        ans += move_min(XB, YB, XC, YC)
        ans += 2
    elif YC > YB:
        p1 = move_min_jama(XA, YA, XB-1, YB, XB, YB)
        p2 = move_min_jama(XA, YA, XB, YB-1, XB, YB)
        ans += min(p1, p2)
        ans += move_min(XB, YB, XC, YC)
        ans += 2
    elif YC == YB:
        ans += move_min_jama(XA, YA, XB-1, YB, XB, YB)
        ans += move_min(XB, YB, XC, YC)

print(ans)