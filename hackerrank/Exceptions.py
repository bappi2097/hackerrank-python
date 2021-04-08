# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------

for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except BaseException as e:
        print("Error Code:", e)