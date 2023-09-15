import sys
import io
sys.setrecursionlimit(10**8)

N = int(input())
go = [[] for _ in range(N)]
for i in range(N-1):
    s, g = map(lambda x: int(x) -1, input().split())
    go[s].append(g)
    go[g].append(s)

max_distance = 0
u = 0

def dfs(start, steps):
    global u
    global max_distance
    if steps > max_distance:
        u = start
        max_distance = steps
    for p in go[start]:
        go[p].remove(start)
        dfs(p, steps+1)
        go[p].append(start)
    
dfs(0, 0)
v = u
max_distance = 0
u = 0
dfs(v, 0)
print(max_distance + 1)