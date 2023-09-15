import sys
import io
sys.setrecursionlimit(10**8)


N = int(input())
road = set([tuple(map(lambda x: int(x) - 1, input().split())) for _ in range (N-1)])
reverse = set()
for r in road:
    reverse.add((r[1], r[0]))
road |= reverse
maxsteps = 0

def dfs(loc, steps, road):
    global maxsteps
    global exlocs
    flag = False
    for i in range(N):
        if (loc, i) in road:
            road.remove((loc, i))
            road.remove((i, loc))
            dfs(i, steps+1, road)
            road.add((i, loc))
            road.add((loc, i))
            flag = True

    if not flag:
        maxsteps = max(maxsteps, steps)
for i in range(N):
    dfs(i, 0, road)
print(maxsteps+1)