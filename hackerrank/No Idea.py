from collections import Counter
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")

# --------end--------

n, m = map(int, input().split())
arrn = Counter(list(map(int, input().split())))
arra = set(list(map(int, input().split())))
arrb = set(list(map(int, input().split())))
total = 0
for i in arrn.items():
    if i[0] in arra:
        total += i[1]
    if i[0] in arrb:
        total -= i[1]
print(total)
