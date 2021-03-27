from itertools import combinations
s, k = input().split()
s = list(s)
s.sort()
for i in range(1, int(k)+1):
    for j in list(combinations(s, i)):
        print("".join(j))