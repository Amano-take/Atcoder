import sys
import io
sys.setrecursionlimit(10**8)

_INPUT = """\
14 5
kittyonyourlap
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
S = input()
ans = ''

def choose_dfs(num, index):
    global ans

    if num == K:
        return ans
    
    
    subS = S[index : N-K+num+1]
    a = min(subS)
    ans += (a)

    choose_dfs(num+1, index + subS.index(a)+ 1)

choose_dfs(0, 0)
print(ans)