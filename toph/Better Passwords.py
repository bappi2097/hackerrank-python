# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------

s = list(input())
s[0] = s[0].upper()
temp = s
count = 0
for i in range(len(s)):
    if s[i] == 'o':
        temp = temp[:i+count] + ['(', ')'] + temp[i+1+count:]
        count += 1
s = temp
for i in range(len(s)):
    if s[i] == 's':
        s[i] = '$'
    elif s[i] == 'i':
        s[i] = '!'
s.append(".")
print("".join(s))