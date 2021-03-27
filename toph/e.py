
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------

n, k = map(int, input().split())
arr = list(map(int, input().split()))
temp = 0
for i in range(n, 0, -1):
    for j in range(n-i+1):
        arrN = arr[j:i+j]
        if max(arrN) - min(arrN) <= k:
            temp = len(arrN)
            break
    if temp != 0:
        break
print(temp)