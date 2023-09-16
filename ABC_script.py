import os
num = 315
for i in range(100):
    n = num + i
    dir_path = './' + str(n)
    if not os.path.isdir(dir_path):
        path = dir_path
        break

abc = ["A", "B", "C", "D", "E", "F"]
line = ["import sys\n", "import io\n", "import math\n", "sys.setrecursionlimit(10**8)\n",
         "_INPUT = \"\"\"\\\n", "\n", "\"\"\"\n","sys.stdin = io.StringIO(_INPUT)\n", "readline=sys.stdin.readline"]

os.makedirs(path)
for alphabet in abc:
    p = path + "/" + alphabet + ".py"
    f = open(p, 'w')
    f.writelines(line)
    f.close
