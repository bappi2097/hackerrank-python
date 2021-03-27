from itertools import groupby
# read and write in text file

# --------start--------
import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
# --------end--------

def sortLen(x):
    return len(x)
s = list(input())
s.sort()
s = [list(g) for k, g in groupby(s)]
s.sort(reverse=True, key=sortLen)
sLen = 3 if len(s) > 3 else len(s)
for i in range(sLen):
    print(s[i][0], "{0}".format(len(s[i])))