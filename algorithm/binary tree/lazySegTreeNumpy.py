from collections import deque
import numpy as np


class lasySegTree():
    def __init__(self, setList:list, funcvv, funcva, funcaa, identityValue=None, identityAction = None):
        """
        遅延セグメント木。モノイドと準同型作用モノイドが必要。\n
        モノイド（単位元の存在と(xy)z = x(yz)\n
        順同型作用モノイド(xy)@a = (x@a)(y@a)(順同型性), x@(a1a2) = (x@a1)@a2(作用素モノイド)
        """
        self.L = 1 << (len(setList) - 1).bit_length()
        self.funcvv = funcvv
        self.funcva = funcva
        self.funcaa = funcaa
        self.identityV = identityValue
        self.identityA = identityAction
        self.lazy = np.repeat(self.identityA, self.L*2 -1)
        self.binaryTree = np.repeat(self.identityV, self.L*2-1)
        self.binaryTree[self.L-1::1] = setList
        self.se = np.repeat(0, self.L-1)
        self.se = np.hstack((self.se, np.array([(i, i+1) for i in range(self.L)])))

        
        
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
            self.rec_section_set(index*2+1, start, end, action)
            self.rec_section_set(index*2+2, start, end, action)
            self.binaryTree[index] = self.funcvv(self.binaryTree[index*2+1], self.binaryTree[index*2+2])
        #完全に一致しない場合
        else:
            return
        
    def stack_section_set(self, start, end, action):
        stack = deque()
        stack.append(0)
        while len(stack) != 0:
            index = stack.pop()
            if index < 0:
                index = - index - 1
                self.binaryTree[index] = self.funcvv(self.binaryTree[index*2+1], self.binaryTree[index*2+2])
                continue
            self.prop(index)
            if start >= end:
                continue
            s, e = self.se[index]
            #完全に包含される場合
            if s >= start and e <= end:
                self.lazy[index] = action
                self.prop(index)
                continue
            #部分的に一致する場合
            elif start < e and end > s:
                stack.append(-index-1)
                stack.append(index*2 + 2)
                stack.append(index*2 + 1)
            #完全に一致しない場合
            else:
                continue

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
        
    
    def stack_query(self, start, end):
        stack = deque([0])
        ans = self.identityV
        while len(stack) != 0:
            index = stack.pop()
            self.prop(index)
            s, e = self.se[index]
            #完全に一致する場合
            if s >= start and e <= end:
                ans = self.funcvv(ans, self.binaryTree[index])
            #部分的に一致する場合
            elif start < e and end > s:
                stack.append(index*2 + 2)
                stack.append(index*2 + 1)
            #完全に一致しない場合
            else:
                continue
        return ans