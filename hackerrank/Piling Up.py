from collections import deque
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------

for i in range(int(input())):
    n = int(input())
    d = deque()
    d.extend(list(map(int, input().split())))
    temp = max(d)
    for j in range(n):
        if d[-1] <= d[0] <= temp:
            temp = d.popleft()
        else:
            if temp >= d[-1]:
                temp = d.pop()
    print("Yes") if len(d) == 0 else print("No")