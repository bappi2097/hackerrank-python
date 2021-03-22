# read and write in text file

# --------start--------
import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
# --------end--------

from collections import deque
d = deque()
for i in range(int(input())):
    s = input().split()
    if s[0] == "append":
        d.append(int(s[1]))
    elif s[0] == "appendleft":
        d.appendleft(int(s[1]))
    elif s[0] == "pop":
        d.pop()
    elif s[0] == "popleft":
        d.popleft()
for x in list(d):
    print(x, end=" ")