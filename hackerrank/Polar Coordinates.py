import cmath
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")
# --------end--------
inp = input()
print(abs(complex(inp)))
print(cmath.phase(complex(inp)))