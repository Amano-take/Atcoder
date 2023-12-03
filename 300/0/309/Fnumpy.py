import bisect
import sys
import io
import math
import numpy as np
import time
# 1 << 大きな数　= 0　になってしまう問題からリタイア。。。
sys.setrecursionlimit(10**8)
f = open("./309/testF.txt")
readline=f.readline

N = int(readline().strip())
high = np.array([[0, 0] for _ in range(N)]) 
mid = np.array([[0, 0] for _ in range(N)])
low = np.array([[0, 0] for _ in range(N)])
highset = np.array([0] * (N+1))
midset =  np.array([0] * (N+1))
lowset =  np.array([0] * (N+1))
total = [(0, 0, 0)] * N
br = bisect.bisect_right
mask = (1 << 20) - 1
for i in range(N):
    h, m, l = sorted(map(int, readline().split()), reverse=True)
    high[i] = [h, i]
    mid[i] = (m, i)
    low[i] = (l, i)
    total[i] = (h, m, l)
high=high[np.argsort(high[:, 0]), :]
mid=mid[np.argsort(high[:, 0]), :]
low=low[np.argsort(high[:, 0]), :]
for i, x in enumerate(zip(high, low, mid)):
    h, m, l = x
    highset[i+1] = highset[i] | ( 1 << h[1])
    midset[i+1] = midset[i] | ( 1 << m[1])
    lowset[i+1] = lowset[i] | ( 1 << l[1])
print(high[0:10, 1])
for i in range(N):
    t = br(high.tolist(),[total[i][0], N+1])
    l = br(mid.tolist(), [total[i][1], N+1])
    m = br(low.tolist(), [total[i][2], N+1])
    if highset[t] | midset[l] | lowset[m] != (1<<N) - 1:
        print(total[int(math.log2((1<<N)-1 - (highset[t] | midset[l] | lowset[m])))-1])
        print(total[i])
        print(i)
        print(t, l, m)
        print(bin(highset[100]))
        print("Yes")
        break
else:
    print("No")
