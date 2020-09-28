# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
deq = deque()
num=0
for i in range(0, n):
    cmd, *number=input().split()
    if (cmd=="append"):
        num=list(map(int, number))[0]
        deq.append(num)
    elif (cmd=="appendleft"):
        num=list(map(int, number))[0]
        deq.appendleft(num)
    elif(cmd=="pop"):
        deq.pop()
    else:
        deq.popleft()
for i in deq:
    print(i, end=" ")
