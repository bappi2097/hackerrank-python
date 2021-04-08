import math
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")

# --------end--------

ab = int(input())
bc = int(input())
print("{0}".format(round(math.degrees(math.atan2(ab, bc)))) + chr(176))