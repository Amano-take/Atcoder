import sys
import io
sys.setrecursionlimit(10**8)

N, K = map(int, input().split())
ans = [0] * N
l = []
for i in range(N):
    m = list(map(lambda x: x % N if x > N else x ,range(i+1, i+1+K)))
    print("?", end=" ")
    print(*m)
    if i == 0:
        ret = int(input())
        first = ret
    else:
        preret = ret
        ret = int(input())
        if ret == -1:
            break
        else:
            if preret == ret:
                l.append(True)
            else:
                l.append(False)

ansano = [1] * N
index = 0
for i in range(N-1):
    a = ans[index]
    b = ansano[index]
    flag = l[index]
    index = (index + K) % N
    if flag:
        ansano[index] = b
        ans[index] = a
    else:
        ansano[index] = not b
        ans[index] = not a

if sum(ans[0:K]) % 2 != ret:
    print("!", end=" ")
    print(*ansano)
else:
    print("!", end=" ")
    print(*ans)

