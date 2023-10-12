import sys
import io

import math


import math


class lasySegTree():
    def __init__(self, setList, funcvv, funcva, funcaa, identityValue=None, identityAction = None):
        """
        遅延セグメント木。モノイドと準同型作用モノイドが必要。\n
        モノイド（単位元の存在と(xy)z = x(yz)\n
        順同型作用モノイド(xy)@a = (x@a)(y@a)(順同型性), x@(a1a2) = (x@a1)@a2(作用素モノイド)
        """
        self.L = 2 ** math.ceil(math.log2(len(setList)))
        self.funcvv = funcvv
        self.funcva = funcva
        self.funcaa = funcaa
        self.identityV = identityValue
        self.identityA = identityAction
        self.lazy = [identityAction for _ in range(self.L * 2 - 1)]

        while len(setList) != self.L:
            setList.append(self.identityV)
        self.binaryTree = [0] * (self.L - 1)
        self.binaryTree.extend(setList)
        self.se = [0] * (self.L - 1)
        self.se.extend([(i, i+1) for i in range(self.L)])

        for i in range(self.L - 2, -1, -1):
            self.binaryTree[i] = self.funcvv(self.binaryTree[2*i + 1], self.binaryTree[2*i + 2])
            self.se[i] = (self.se[2*i + 1][0] , self.se[2*i+2][1])
        
    def show(self):
        j = 1
        for i in range(self.L*2-1):
            print(self.binaryTree[i], end=" ")
            if i == 2 ** j - 2:
                j += 1
                print()
        print("------")
        j = 1
        for i in range(self.L*2-1):
            print(self.se[i], end=" ")
            if i == 2 ** j - 2:
                j += 1
                print()

    def set(self, index, value):
        """
        indexは0はじまり
        """
        index = self.L - 1 + index
        self.binaryTree[index] = value
        while True:
            index = (index - 1 ) // 2
            self.binaryTree[index] = self.func(self.binaryTree[2*index + 1], self.binaryTree[2*index + 2])
            if index == 0:
                break

    def section_set(self, start, end, action):
        self.rec_section_set(0, start, end, action)
    
    def rec_section_set(self, index, start, end, action):
        self.prop(index)
        if start >= end:
            return
        s, e = self.se[index]
        #完全に包含される場合
        if s >= start and e <= end:
            self.lazy[index] = action
            self.prop(index)
            return
        #部分的に一致する場合
        elif start < e and end > s:
            mid = self.se[index*2+1][1]
            self.rec_section_set(index*2+1, start, end, action)
            self.rec_section_set(index*2+2, start, end, action)
            self.binaryTree[index] = self.funcvv(self.binaryTree[index*2+1], self.binaryTree[index*2+2])
        #完全に一致しない場合
        else:
            return

    def prop(self, index):
        if not self.lazy[index] == self.identityA:
            self.binaryTree[index] = self.funcva(self.binaryTree[index], self.lazy[index])
            if index <= self.L - 2:
                self.lazy[index*2+1] = self.funcaa(self.lazy[index*2 + 1], self.lazy[index])
                self.lazy[index*2+2] = self.funcaa(self.lazy[index*2 + 2], self.lazy[index])
            self.lazy[index] = self.identityA
    
    def query(self, start, end):
        """
        [start, end)\n
        start, end それぞれ0はじまり
        """
        return self.recquery(0, start, end)

    def recquery(self, index, start, end):
        self.prop(index)
        if start == end:
            return self.identityV
        s, e = self.se[index]
        #完全に一致する場合
        if s >= start and e <= end:
            return self.binaryTree[index]
        #部分的に一致する場合
        elif start < e and end > s:
            return self.funcvv(self.recquery(index*2+1, start, end), self.recquery(index*2+2, start, end))
        #完全に一致しない場合
        else:
            return self.identityV
        
sys.setrecursionlimit(10**8)
_INPUT = """\
7 6
1101110
2 1 7
2 2 4
1 3 6
2 1 7
1 4 7
2 1 7
"""
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline
N, M = map(int, input().split())


def funcvv(s, t):
    if s is None and t is None:
        return None
    elif s is None:
        return t
    elif t is None:
        return s
    else:
        return "".join([s, t])

def funcaa(a, b):
    if a is None and b is None:
        return None
    elif a is None:
        return b
    elif b is None:
        return a
    else:
        return None
    
def funcva(v, a):
    if a is None:
        return v
    else:
        ans = bin(2**len(v) - 1 - int(v, 2))[2:]
        if len(ans) == len(v):
            return ans
        else:
            t = "0" * (len(v) - len(ans))
            return "".join([t, ans])
    
def count(s):
    a = list(map(int, list(s)))
    max = 0
    t = 0
    for i in range(len(a)):
        if a[i] == 1:
            t+=1
            if t > max:
                max = t
        else:
            t = 0
    return max

S = list(input())
lst = lasySegTree(S, funcvv, funcva, funcaa, identityValue="0")
for _ in range(M):
    x, s, e = map(int, input().split())
    s -= 1
    if x == 1:
        lst.section_set(s, e, 1)
    else:
        print(count(lst.query(s, e)))
