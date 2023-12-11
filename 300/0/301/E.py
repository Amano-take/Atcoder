import sys
import io
import math
from collections import deque, defaultdict as ddict
sys.setrecursionlimit(10**8)
_INPUT = """\
5 10 2000000
S.o..ooo..
..o..o.o..
..o..ooo..
..o..o.o..
..o..ooo.G
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
H, W, T = map(int, readline().split())
board = [list(readline().strip()) for _ in range(H)]

queue = deque([])
cookied = ddict(int)
c = 0
for x in range(H):
    for y in range(W):
        if board[x][y] == 'S':
            sx, sy = x, y
        elif board[x][y] == 'G':
            gx, gy = x, y
        elif board[x][y] == 'o':
            cookied[(x, y)] = c
            c += 1
queue.append((T, (sx, sy), 0))
visited = [[(-1, 0) for _ in range(W)]  for _ in range(H)]
visited[sx][sy] = (0, 0)
#bfs
while len(queue) > 0:
    t, (x, y), cookie = queue.popleft()
    cookienum = bin(cookie).count('1')
    if t == 0 or (visited[x][y][0] >= t and bin(visited[x][y][1]).count("1") > cookienum) or (visited[x][y][0] > t and bin(visited[x][y][1]).count("1") >= cookienum):
        continue

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if board[nx][ny] == '#':
            continue

        elif board[nx][ny] == 'o':
            cindex = cookied[(nx, ny)]
            if cookie & (1 << cindex) == 0:
                c = cookie + (1 << cindex)
            else:
                c = cookie
        else:
            c = cookie

        if bin(visited[nx][ny][1]).count("1")  < bin(c).count("1") or visited[nx][ny][0] < t - 1:
            if bin(visited[nx][ny][1]).count("1")  < bin(c).count("1"):
                visited[nx][ny] = (t - 1, c)
            queue.append((t - 1, (nx, ny), c))

if visited[gx][gy][0] != -1:
    print(bin(visited[gx][gy][1]).count("1"))
else:
    print(-1)