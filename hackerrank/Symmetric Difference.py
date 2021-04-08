# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")

# --------end--------

input()
m = set(list(map(int, input().split())))
input()
n = set(list(map(int, input().split())))
mn = sorted(m.symmetric_difference(n))
for i in mn:
    print(i)