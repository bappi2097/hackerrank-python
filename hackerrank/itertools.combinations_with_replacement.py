from itertools import combinations_with_replacement
s, k = input().split()
s = list(s)
s.sort()
for i in list(combinations_with_replacement(s, int(k))):
    print("".join(i))