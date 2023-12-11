import sys
import io
import math
sys.setrecursionlimit(10**8)
_INPUT = """\
1?1??0001????1??110?1?11???010010???00??0??1???011????
15823311453062150
"""


sys.stdin = io.StringIO(_INPUT)
readline=sys.stdin.readline
S = list(readline().strip())
N = int(readline())
SN = bin(N)[2:]

if len(SN) < len(S):
    SN = "0" * (len(S) - len(SN)) + SN
if len(SN) > len(S):
    N = (1 << len(S)) - 1
    SN = bin(N)[2:]
assert len(S) == len(SN)

diff = -1
recent = -1
for i in range(len(S)):

    if diff != -1:
        if S[i] == "?":
            S[i] = "1"
        continue

    if S[i] == "?":
        if SN[i] == "1":
            recent = i
        continue

    elif S[i] != SN[i]:
        diff = i
        large = S[i] > SN[i]


if diff == -1:
    print(N)
    sys.exit()
else:
    if large:
        if recent == -1:
            print(-1)
            sys.exit()
        else:
            ans = []
            for i in range(len(S)):
                if S[i] == "?":
                    if i < recent:
                        ans.append(SN[i])
                    elif i == recent:
                        ans.append("0")
                    else:
                        ans.append("1")
                else:
                    ans.append(S[i])
            print(int("".join(ans), 2))
    else:
        print(int("".join(S), 2))