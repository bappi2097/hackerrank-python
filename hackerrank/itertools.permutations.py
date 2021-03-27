from itertools import permutations
s, k = input().split()
s = list(s)
s.sort()
perms = permutations(s, int(k))
for i in perms:
    print("".join(i[0:]))