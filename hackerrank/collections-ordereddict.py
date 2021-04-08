from collections import OrderedDict
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")

# --------end--------
order_dict = OrderedDict()
for _ in range(int(input())):
    inp = input().split()
    s = " ".join(inp[:len(inp)-1])
    if s in order_dict.keys():
        order_dict[s] = order_dict[s]+int(inp[len(inp)-1])
    else:
        order_dict[s] = int(inp[len(inp) - 1])
for i in order_dict.items():
    print(i[0], i[1])