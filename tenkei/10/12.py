import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
5 5
42
2 3 4 3 4
2 3 2 3 2
1 4 1
2 4 1 2 2
1 1 2
1 4 5
1 3 3
2 4 2 1 3
1 3 5
2 2 4 2 3
2 2 4 2 5
2 3 4 5 1
2 3 1 2 2
2 3 1 1 2
2 2 4 5 2
2 3 2 5 3
1 4 3
2 3 3 3 5
2 3 1 3 2
1 1 5
2 4 4 5 3
1 1 4
2 1 3 2 5
2 4 3 1 4
2 2 3 3 3
1 2 1
1 2 5
2 1 4 5 3
2 4 4 2 5
2 4 2 2 4
1 2 2
2 4 1 5 2
1 2 4
2 3 1 4 1
1 4 4
2 3 2 2 1
2 1 1 5 2
1 4 2
2 4 2 3 5
1 3 2
1 3 4
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

#O(Q*HW)で処理しないと間に合わなさそう
#連結成分保持
#<= 発想はいい！！　ユニオンファインド木！！

H, W = map(int, input().split())
Q = int(input())
m = []
#Q
for _ in range(Q):
    t, *L = map(int, input().split())
    if t == 1:
        px, py = L
        flag = False
        poplist = []
        if len(m) == 0:
            m.append([(px, py)])
            continue
        for index, x in enumerate(m):
            for p in x:
                if abs(px - p[0]) + abs(py - p[1]) == 1 and not flag:
                    x.append((px, py))
                    flag = True
                    pre = x
                    break
                elif abs(px - p[0]) + abs(py - p[1]) == 1:
                    pre.extend(x)
                    poplist.append(index)
                    break
        for p in reversed(poplist):
            m.pop(p)
        if not flag:
            m.append([(px, py)])

    else:
        px, py, qx, qy = L
        flag = False
        for index, x in enumerate(m):
            if (px, py) in x:
                mem = index
                flag = True
        if flag and (qx, qy) in m[mem]:
            print("Yes")
            continue
        print("No")
