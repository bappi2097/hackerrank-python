# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------

def func(x):
    x = list(str(x))
    sumN = 0
    for i in x:
        sumN += int(i)**2
    return sumN

n = int(input())
dict = {}
temp = n
while True:
    temp = func(temp)
    if temp == 1:
        print("NO CYCLE")
        break
    elif temp == n:
        print("FULL CYCLE")
        break
    elif temp in dict.keys():
        print("PARTIAL CYCLE")
        break
    else:
        dict[temp] = True