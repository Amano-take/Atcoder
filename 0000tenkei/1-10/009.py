import sys
import io
import math
from bisect import bisect_left
sys.setrecursionlimit(10**8)

_INPUT = """\
40
298750376 229032640
602876667 944779015
909539868 533609371
231368330 445484152
408704870 850216874
349286798 30417810
807260002 554049450
40706045 380488344
749325840 801881841
459457853 66691229
5235900 8100458
46697277 997429858
827651689 790051948
981897272 271364774
536232393 997361572
449659237 602191750
294800444 346669663
792837293 277667068
997282249 468293808
444906878 702693341
894286137 845317003
27053625 926547765
739689211 447395911
902031510 326127348
582956343 842918193
235655766 844300842
438389323 406413067
862896425 464876303
68833418 76340212
911399808 745744264
551223563 854507876
196296968 52144186
431165823 275217640
424495332 847375861
337078801 83054466
648322745 694789156
301518763 319851750
432518459 772897937
630628124 581390864
313132255 350770227
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]
ans = 1

def three2angle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    vector1x = x2 - x1
    vector1y = y2 - y1
    vector2x = x3 - x1
    vector2y = y3 - y1
    vector3x = x3 - x2
    vector3y = y3 - y2

    cost1 = (vector1x * vector2x + vector1y * vector2y) / (math.sqrt(vector1x**2 + vector1y**2) * math.sqrt(vector2x**2 + vector2y**2))
    cost2 = -(vector1x * vector3x + vector1y * vector3y) / (math.sqrt(vector1x**2 + vector1y**2) * math.sqrt(vector3x**2 + vector3y**2))
    cost3 = (vector2x * vector3x + vector2y * vector3y) / (math.sqrt(vector2x**2 + vector2y**2) * math.sqrt(vector3x**2 + vector3y**2))

    return min(cost1, cost2, cost3)

def two2angle(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    vector1x = x2 - x1
    vector1y = y2 - y1
    vector2x = 1
    vector2y = 0

    cost1 = (vector1x * vector2x + vector1y * vector2y) / (math.sqrt(vector1x**2 + vector1y**2) * math.sqrt(vector2x**2 + vector2y**2))

    if vector1y < 0:
        return math.pi * 2 - math.acos(cost1)
    return math.acos(cost1)

def angle(an):
    if an > math.pi:
        return math.pi * 2 - an
    return an
"""for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            ans = min(ans, three2angle(point[i], point[j], point[k]))"""

for i in range(N):
    ll = []
    for j in range(N):
        if i != j:
            ll.append(two2angle(point[i], point[j]))
    
    ll.sort()
    for j in range(N-1):
        if ll[j] > math.pi:
            index = bisect_left(ll, ll[j]-math.pi)
        else:
            index = bisect_left(ll, ll[j]+ math.pi)

        if index == 0:
            ans = max(ans, angle(abs(ll[j] - ll[index])))
        elif index == len(ll):
            ans = max(ans, angle(abs(ll[j] - ll[index-1])))
        else:
            ans = max(ans, angle(abs(ll[j] - ll[index])), angle(abs(ll[j] - ll[index-1])))




print(math.degrees(ans))

