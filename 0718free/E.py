import sys
import io

def main():

    read = sys.stdin.read
    readline = sys.stdin.readline
    readlines = sys.stdin.readlines
    for i, l in enumerate(readlines()):
        if i == 0:
            N = int(l)
        elif i==1:
            nums = [s for s in map(int, l.split()[0])]
    ans = 0
    for i, l in enumerate(nums):
        ans += nand(nums[i:])

    print(ans)

def nand(nums):
    ans_num = 0
    for i,num in enumerate(nums):
        if i==0:
            ans = num
        else:
            ans = not (ans and num)
        ans_num += ans
    return ans_num

if __name__ == "__main__":
    main()