from collections import defaultdict
import sys
import io
import math
inf = float("inf")
sys.setrecursionlimit(10**8)
def boyer_moore(text, pattern):
    skip = {}
    ans = []
    #パターンの文字に応じたずらしを記録
    for i in range(len(pattern) - 1):
        skip[pattern[i]] = len(pattern) - i -1

    i = len(pattern) - 1    #探索初期値はテキストとパターンの先頭が合うようにしたときの末尾になるように設定

    while i < len(text):
        match = True    #patternと一致すると仮定

        for j in range(len(pattern)):
            #patternを順に1文字ずつ比較する
            if text[i - j] != pattern[-1-j]:
                match = False   #不一致
                break   #探索箇所を次に移行するため，これ以上の探索はしない

        if match:   #すべて一致した ⇒ 発見 ⇒ 探索終了
            ans.append(i - len(pattern) + 1) #末尾から探索しているため先頭の位置を返す処理を行う
        if text[i] in skip:
            i += skip[text[i]]    #先ほどの結果から得られた探索箇所をずらす分を足し合わせる
        else:
            i += len(pattern)   #ずらす対象がとくに見当たらなければ，パターンの文字数だけずらす
    
    return ans

_INPUT = """\
12 2
XYXYYXYYYXXYXY
XYXY
"""
sys.stdin = io.StringIO(_INPUT)
readline=lambda: sys.stdin.readline().strip()
N, M = map(int, readline().split())
S = list(readline())
T = readline()
cand = boyer_moore(S, T)
rest = set(range(len(S)))
ex = set()
while len(cand) > 0 and len(rest) > 0:
    next = set()
    for c in cand:
        if c in ex:
            continue

        #cが当てはまる
        for i in range(len(T)):
            if S[i+c] == T[i] or S[i+c] == "#":
                pass
            else:
                break
        else:
            ex.add(c)
            flag = False
            for i in range(len(T)):
                if S[i+c] != "#":
                    flag = True
                    rest.discard(i+c)
                    S[i+c] = "#"
            
            if flag:
                a = set(range(max(0, c-len(T)+1), min(c+len(T), len(S) - len(T)+ 1))) 
                next |= a

    cand = next - ex

if len(rest) == 0:
    print("Yes")
else:
    print("No")