import sys
import io
import heapq
sys.setrecursionlimit(10**8)
_INPUT = """\
1 aaaa
aaabb
"""
sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline

a, b = input().split()
ans = []
n = int(a)
lenb = len(b)
for j in range(n):
    s = readline().strip()
    if lenb == len(s):
        flag = False
        for s1, s2 in zip(b, s):
            if s1 != s2 and flag:
                break
            elif s1 != s2:
                flag = True
        else: ans.append(j+1)
    elif lenb == len(s)+1:
        flag = False
        t = 0
        for i in range(lenb):
            if t == len(s):
                continue
            if b[i] != s[t] and flag:
                break
            elif b[i] != s[t]:
                flag = True
            else:
                t += 1
        else:
            ans.append(j+1)
    elif len(s) == lenb+1:
        flag = False
        t = 0
        for i in range(len(s)):
            if t == lenb:
                continue
            if b[t] != s[i] and flag:
                break
            elif b[t] != s[i]:
                flag = True
            else:
                t += 1
        else:
            ans.append(j+1)
print(len(ans))
print(*ans)