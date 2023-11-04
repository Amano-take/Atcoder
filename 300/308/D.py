import sys
import io
import math
from collections import defaultdict
sys.setrecursionlimit(10**8)
_INPUT = """\
2 3
sns
euk
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
sunuke = ["s", "n", "u", "k", "e", "s"]
di = defaultdict(str)
for i in range(len(sunuke)- 1):
    di[sunuke[i]] = sunuke[i+1]
H, W = map(int, readline().split())
board = [list(readline().strip()) for _ in range(H)]
ex = [[False] * W for _ in range(H)]
ex[0][0] = True
def dfs(p, s, ex):
    if p == (W-1, H-1):
        return True
    else:
        x, y = p
        nexts = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        for nx, ny in nexts:
            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                continue
            if board[ny][nx] == di[s] and ex[ny][nx] == False:
                ex[ny][nx] = True
                b = dfs((nx, ny), di[s], ex)
                if b:
                    return True
        return False

b = dfs((0, 0), "s", ex)
if b:
    print("Yes")
else:
    print("No")