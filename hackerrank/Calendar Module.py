import calendar
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------

mm, dd, yyyy = map(int, input().split())
print(list(calendar.day_name)[calendar.weekday(yyyy, mm, dd)].upper())