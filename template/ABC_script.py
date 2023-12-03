import os
num = 300
for i in range(100):
    n = num + i
    dir_path = './' + str((n//100) * 100) + "/" + str((n - (n//100)*100) // 10 * 10) + "/" + str(n)
    if not os.path.isdir(dir_path):
        path = dir_path
        break

abc = ["A", "B", "C", "D", "E", "F", "G"]
line = ["import sys, io\n", "import math, heapq, bisect\n", "from collections import deque, defaultdict as ddict\n", 
        "from itertools import product\n", "inf = float(\"inf\")\n", "sys.setrecursionlimit(10**8)\n",
         "_INPUT = \"\"\"\\\n", "\n", "\"\"\"\n","sys.stdin = io.StringIO(_INPUT)\n", "input=lambda: sys.stdin.readline().strip()"]

os.makedirs(path)
for alphabet in abc:
    p = path + "/" + alphabet + ".py"
    f = open(p, 'w')
    f.writelines(line)
    f.close
