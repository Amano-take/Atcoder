import sys
import io
from collections import defaultdict

sys.setrecursionlimit(15)
ans = 0
def solve():
    _INPUT = """\
    10 14
    1 2 1
    1 10 1
    2 3 1
    3 4 4
    4 7 2
    4 8 1
    5 8 1
    5 9 3
    6 8 1
    6 9 5
    7 8 1
    7 9 4
    9 10 3
    1 2 1
    """
    sys.stdin = io.StringIO(_INPUT)
    readline = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B, C = map(int, readline().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
        
    def dfs(s, exs, cost):
        global ans
        if cost > ans:
            ans = cost
        for next, length in graph[s]:
            if (1<<(next-1)) & exs == 0:
                dfs(next, exs|(1<<(next-1)), cost+length)

    for i in range(1, N+1):
        dfs(i, 1<<(i-1), 0)

    print(ans)

solve()