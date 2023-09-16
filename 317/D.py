import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = """\
10
1878 2089 16
1982 1769 13
2148 1601 14
2189 2362 15
2268 2279 16
2394 2841 18
2926 2971 20
3091 2146 20
3878 4685 38
4504 4617 29
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N = int(input())
XL = []
total = 0
enemy = 0
ans = 0
for _ in range(N):
    X, Y, Z = map(int, input().split())
    total += Z
    if X < Y:
        XL.append(((Y+1-X)//2, Z))
        enemy += Z
        ans += X
target = enemy - (total - 1) // 2
XL.sort(key=lambda x: x[0] / x[1])



def dfs(index, rest, cost, XL):
    global ans
    if index == len(XL) -1:
        return 
    if rest <= 0 and cost < ans:
        ans = cost
        return
    
    elif rest > 0:
        if XL[index+1][0] < rest:
            dfs(index+1, rest-XL[index+1][1], cost+XL[index+1][0], XL)
        else:
            dfs(index+1, rest, cost, XL)
            dfs(index+1, rest-XL[index+1][1], cost+XL[index+1][0], XL)

dfs(-1, target, 0, XL)
print(ans)
        

