import sys
import io
from collections import defaultdict as ddict
sys.setrecursionlimit(10**8)

_INPUT = """\
3
snuke
snuke
rng
"""
sys.stdin = io.StringIO(_INPUT)
d = dict()
N = int(input())

def z_alg(s):
    z = [0]*len(s)
    z[0] = len(s)
    l = r = 0
    for i in range(1,len(s)):
        print(z)
        if z[i-l] < r-i:
            print("YES")
            z[i] = z[i-l]
        else:
            print("No")
            r = max(r,i)
            while r < len(s) and s[r] == s[r-i]:
                r += 1
            z[i] = r-i
            l = i
    print(z)



z_alg("abcabcabc")