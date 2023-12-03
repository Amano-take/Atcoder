import sys
import io

def main():
    read = sys.stdin.read
    readline = sys.stdin.readline
    readlines = sys.stdin.readlines
    flagA, flagB, flagC = False, False, False
    for i, l in enumerate(readlines()):
        if i==0:
            N = int(l)
        else:
            for i, s in enumerate(l.strip()):
                if s == 'A':
                    flagA = True
                elif s == 'B':
                    flagB = True
                elif s == 'C':
                    flagC = True
                if flagA and flagB and flagC :
                    print(i+1)
                    return 
                

if __name__ == "__main__":
    main()