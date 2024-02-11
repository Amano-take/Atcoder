import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
3
7 3 200000
3 2 100000
5 3 150000
"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())
task = []
for _ in range(N):
    d, c, s = map(int, input().split())
    task.append((d, c, s))

DAY = 8
dp = [[0] * DAY for _ in range(N+1)]
#i個めまでで日数がj日までの時に得られる最大の報酬

for i in range(1, N+1):
    d, c, s = task[i-1]
    for j in range(DAY):
        dp[i][j] += dp[i-1][j]
    for j in range(c, d):
        dp[i][j] = max(dp[i-1][j-c+1]+s, dp[i-1][j])
        
    for j in range(1, DAY):
        dp[i][j] = max(dp[i][j], dp[i][j-1])
    print(dp)

print(dp)