import sys
import io
sys.setrecursionlimit(10**8)

N = int(input())
task = []
for _ in range(N):
    d, c, s = map(int, input().split())
    task.append((d, c, s))

#締め切りが短い順に並べると、その仕事を新たに着手するかしないかの二択にできる
#ソートしていないと、以前の選択に影響が出る。この仕事を選んで、以前の仕事をなかったことに。。。
task.sort(key=lambda x: x[0])

DAY = 5001
dp = [[0] * DAY for _ in range(N+1)]
#i個めまでで仕事日数がちょうどj日までの時に得られる最大の報酬

for i in range(1, N+1):
    d, c, s = task[i-1]
    for j in range(DAY):
        if j < c or j > d:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + s)
    for j in range(DAY-1):
        dp[i][j+1] = max(dp[i][j], dp[i][j+1])

print(max(dp[N]))