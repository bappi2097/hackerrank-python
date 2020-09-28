from itertools import combinations_with_replacement
s, r=input().split()
s=list(s)
s.sort()
comb=list(combinations_with_replacement(s, int(r)))
for i in comb:
    print("".join(i))
