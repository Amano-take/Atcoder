import sys
import io
from collections import defaultdict
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
3
1 1 3 2 3 2 2 3 1
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
N = int(input())
As = map(int, readline().split())
ans = defaultdict(list)
pri = []
for i,a in enumerate(As):
    ans[a].append(i)
    if len(ans[a]) == 2:
        pri.append(a)
print(*pri)