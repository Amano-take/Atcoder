import sys
import io
sys.setrecursionlimit(10**8)



N = int(input())
dic = {1:[], 2:[]}
for i in range(N):
    c, p = map(int, input().split())
    if c in dic:
        dic[c].append((i, p))

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    ans = []
    for k in range(1, 3):
        ans.append(sum(map(lambda x: x[1], filter(lambda x: x[0] >= l-1 and x[0] <= r-1, dic[k]))))

    print(*ans)