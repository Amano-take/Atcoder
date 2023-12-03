import sys
import io
from collections import deque
from collections import defaultdict as ddict
import heapq
import bisect

sys.setrecursionlimit(10**8)
_INPUT = """\
2
1 1
1000000000000000000 1000000000000000000
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
TD = ddict(list)
time = set()
for _ in range(N):
    T, D = map(int, readline().split())
    TD[T].append(T+D)
    time.add(T)
timer = sorted(time)
t = 1
hq = []
ans = 0
while True:
    for end in TD[t]:
        heapq.heappush(hq, end)
    while len(hq) != 0:
        e = heapq.heappop(hq)
        if e < t:
            continue
        else:
            ans += 1
            break
    if len(hq) == 0:
        index = bisect.bisect_right(timer, t)
        if index == len(timer):
            break
        else:
            t = timer[index]
    else:
        t += 1
print(ans)