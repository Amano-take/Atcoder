import bisect
import sys
import io
import math
import time
sys.setrecursionlimit(10**8)
f = open("./309/testF.txt", mode="r")
readline=f.readline
N = int(readline().strip())
high = [(0, 0)]* (N) 
mid = [(0, 0)]* (N)
low = [(0, 0)]* (N)
highset = [0] * (N+1)
midset =  [0] * (N+1)
lowset =  [0] * (N+1)
total = [(0, 0, 0)] * N
br = bisect.bisect_left
mask = (1 << 20) - 1
for i in range(N):
    h, m, l = sorted(map(int, readline().split()), reverse=True)
    high[i] = (h, i)
    mid[i] = (m, i)
    low[i] = (l, i)
    total[i] = (h, m, l)
high.sort(key=lambda x: x[0])
mid.sort(key=lambda x: x[0])
low.sort(key=lambda x: x[0])
print("koko")
ttbefore = time.time()
for i, x in enumerate(zip(high, low, mid)):
    h, m, l = x
    highset[i+1] = highset[i] | ( 1 << h[1])
    midset[i+1] = midset[i] | ( 1 << m[1])
    lowset[i+1] = lowset[i] | ( 1 << l[1])
print("koko")
ttafter= time.time()
print(ttafter - ttbefore)
for i in range(N):
    t = br(high, (total[i][0], N+1))
    l = br(mid, (total[i][1], N+1))
    m = br(low, (total[i][2], N+1))
    if highset[t] | midset[l] | lowset[m] != (1<<N) - 1:
        print("Yes")
        break
else:
    print("No")
