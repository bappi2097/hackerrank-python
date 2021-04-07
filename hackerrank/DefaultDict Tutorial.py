from collections import defaultdict
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------

cnt = 0
dd = defaultdict(list)
n, m = map(int, input().split())
for _ in range(n):
    cnt += 1
    dd[input()].append(cnt)
for _ in range(m):
    t = input()
    if t in dd.keys():
        for i in dd[t]:
            print(i, end=" ")
        print("")
    else:
        print(-1)