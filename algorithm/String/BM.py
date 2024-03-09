def boyer_moore(text, pattern):
    skip = {}
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
            return i - len(pattern) + 1 #末尾から探索しているため先頭の位置を返す処理を行う
        if text[i] in skip:
            i += skip[text[i]]    #先ほどの結果から得られた探索箇所をずらす分を足し合わせる
        else:
            i += len(pattern)   #ずらす対象がとくに見当たらなければ，パターンの文字数だけずらす

import collections 

def create_bad_calacter_heuristic_table(t):
    # パターンの各文字について、その文字がパターンの中で最後に出現する位置を記録
    table = collections.defaultdict(lambda: -1)
    for k, c in enumerate(t):
        table[c] = k
    return table

#print(create_bad_calacter_heuristic_table("abracadabra"))
#{'a': 10, 'b': 8, 'r': 9, 'c': 4, 'd': 6})

def create_good_suffix_heuristic_table(t):
    f = [0] * (len(t) + 1)
    j = len(t) + 1
    f[len(t)] = j
    # https://qiita.com/t_fuki/items/408fe87dceb4c88bd036#good-suffix-heuristic
    # G1[j] = j - max { k | T[k:k+|T|-j] == T[j:||T|] and T[k-1] != T[j-1] }
    for k in reversed(range(1, len(t) + 1)):
        while j <= len(t) and t[k - 1] != t[j - 1]:
            j = f[j]
        f[k - 1] = j - 1
        j -= 1
    print(f)

    table = [0] * (len(t) + 1)
    for k in reversed(range(1, len(t) + 1)):
        j = f[k]
        while j <= len(t) and t[k - 1] != t[j - 1]:
            if table[j] == 0:
                table[j] = j - k
            j = f[j]

    k = f[0]
    for j in range(len(t) + 1):
        if table[j] == 0:
            table[j] = k
        if j == k:
            k = f[k]

    return table

print(create_good_suffix_heuristic_table("abrabra"))
#[4, 4, 4, 4, 4, 7, 7, 1]
def boyer_moore_search(s, t):
    bad_calacter_heuristic_table = create_bad_calacter_heuristic_table(t)
    good_suffix_heuristic_table = create_good_suffix_heuristic_table(t)
    i = 0
    res = []
    while i + len(t) <= len(s):
        j = len(t) - 1
        k = i
        while j >= 0 and s[i + j] == t[j]:
            j -= 1
        if j < 0:  # 検索パターンと一致しているため出力に追加、Bad Character Heuristicが使えないためシフト幅はGood Suffix Heuristicにより決定
            res.append(i)
            shift = good_suffix_heuristic_table[0]
        else:
            shift = max(j - bad_calacter_heuristic_table[s[i + j]], good_suffix_heuristic_table[j + 1])  # 2つの規則のうちシフト幅が大きい方を最終的なシフト幅とする
        i += shift
    return res