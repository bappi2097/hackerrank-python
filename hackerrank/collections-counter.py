from collections import Counter
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------

input()
cntr = Counter(map(int, input().split()))
sumN = 0
for _ in range(int(input())):
    inp = list(map(int, input().split()))
    if cntr[inp[0]] != 0:
        sumN += inp[1]
        cntr[inp[0]] -= 1
print(sumN)