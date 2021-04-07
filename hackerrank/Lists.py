# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------
lst = list()
for _ in range(int(input())):
    cmd, *arr = input().split()
    if cmd == "insert":
        lst.insert(int(arr[0]), int(arr[1]))
    elif cmd == "remove":
        lst.remove(int(arr[0]))
    elif cmd == "append":
        lst.append(int(arr[0]))
    elif cmd == "sort":
        lst.sort()
    elif cmd == "pop":
        lst.pop()
    elif cmd == "reverse":
        lst.reverse()
    elif cmd == "print":
        print(lst)