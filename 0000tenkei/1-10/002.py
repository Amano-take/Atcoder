import sys
import io
sys.setrecursionlimit(10**8)



def parentheses(N):
    if N==2:
        return {"()"}
    if N % 2 != 0:
        return set()
    ans = set(map(lambda m: '(' + m + ')', parentheses(N-2)))
    for i in range(2, N-1, 2):
        for j in parentheses(i):
            ans |= set(map(lambda m: m + j, parentheses(N - i)))

    return ans

N = int(input())
ans = list(parentheses(N))
ans = sorted(ans)
for i in ans:
    print(i)
