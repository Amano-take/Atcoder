import sys
import io
import math
sys.setrecursionlimit(10**8)



S = input()

anslist = [ "ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]

for i in anslist:
    if S == i:
        print("Yes")
        break
else:
    print("No")