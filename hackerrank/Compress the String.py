from itertools import groupby

# read and write in text file

# --------start--------
import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
# --------end--------


s = list(input())
for i in [list(g) for k, g in groupby(s)]:
    print("({0}, {1})".format(len(i), i[0]), end=" ")