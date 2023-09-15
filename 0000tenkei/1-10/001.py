import sys
import io
sys.setrecursionlimit(10**8)

def dfs(score, cut):
    global highscore
    if len(cut) == K+1:
        tmp = min(score, L-A_list[cut[-1]])
        if tmp > highscore:
            highscore = tmp
        return
    
    for i in range(cut[-1]+1, N-K+len(cut)+1):
        tmp = min(score, A_list[i] - A_list[cut[-1]])
        if tmp > highscore and (L - A_list[i])/(K - len(cut) + 1) >= highscore:
            cut.append(i)
            dfs(tmp, cut)
            cut.pop()
        else:
            continue


N, L = map(int, input().split())
K = int(input().strip())
A_list = list(map(int, [0] + input().split()))
highscore = 0
dfs(L, [0])
print(highscore)

        