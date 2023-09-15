import sys
import io
from collections import defaultdict as ddict

sys.setrecursionlimit(10**8)

#ある中心となる点があって、その点からそれぞれ別方向にu, v, wがあるときに

N = int(input())
tree = ddict(list)
chnum = [1] * N
parentl = [0] * N
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

#木のdfsは親も指定
def dfs(sect, parent):
    parentl[sect-1] = parent
    for ch in tree[sect]:
        if ch != parent:
            dfs(ch, sect)
            chnum[sect-1] += chnum[ch-1]

def calc(ll):
    dp = [[0] * 4 for _ in range(len(ll)+1)]
    dp[0][0] = 1
    for i in range(len(ll)):
        for j in range(4):
            if j != 0:
                dp[i+1][j] += dp[i][j-1] * ll[i]
            dp[i+1][j] += dp[i][j]
    return dp[-1][3]

dfs(1, 0)
ans = 0

for i in range(1, N+1):
    v = []
    n = N-1
    for j in tree[i]:
        if j != parentl[i-1]:
            v.append(chnum[j-1])
            n -= chnum[j-1]
    v.append(n)
    ans += calc(v)

print(ans)