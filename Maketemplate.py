import os

num = 321
new_dir_path = './' + str(num)

try:
    os.mkdir(new_dir_path)
except:
    exit()

ABC = ["A", "B", "C", "D", "E", "F", "G", "Ex"]
for alphabet in ABC:
    new_file_path = new_dir_path + "/" + alphabet + ".py"
    with open(new_file_path, mode="w") as f:
        f.write("""\
import sys
import io
sys.setrecursionlimit(10**8)
_INPUT = \"\"\"\\

\"\"\"
sys.stdin = io.StringIO(_INPUT)
readline = sys.stdin.readline""")
        
