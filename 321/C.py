import sys
import io
import bisect
import itertools
sys.setrecursionlimit(10**8)
_INPUT = """\
777
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
dp = [[0] * 10 for i in range(10)]
dp[0] = [1 for _ in range(10)]

for i in range(1, 10):
    for s in range(1, 10):
        for k in range(0, s):
            dp[i][s] += dp[i-1][k]

dp[0][0] = 0
ruiseki = [0] * 100
for i in range(10):
    for j in range(10):
        ruiseki[i*10+j] = ruiseki[i*10+j-1] + dp[i][j]
ans = []
index = bisect.bisect_left(ruiseki, N)
start = (index)%10
ans.append(start)
radi = (index) // 10 + 1
N -= ruiseki[index-1]
numbers = [i for i in range(start-1, -1, -1)]
for pair in reversed(list(itertools.combinations(numbers, radi-1))):
    N-=1
    if N == 0:
        for p in pair:
            ans.append(p)
print("".join(map(str, ans)))
            
