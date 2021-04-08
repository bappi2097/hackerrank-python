from collections import namedtuple
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------

def marksSum(marks):
    sumNo = 0
    for i in marks:
        sumNo += int(i.MARKS)
    return sumNo

n = int(input())
Student = namedtuple("Student", " ".join(input().split()))
marks = list()
for i in range(n):
    a, b, c, d = input().split()
    marks.append(Student(a, b, c, d))
print(marksSum(marks)/len(marks))
