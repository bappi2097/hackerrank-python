from itertools import groupby
s=list(input())
gpb=[list(g) for k,g in groupby(s)]
for i in gpb:
    print("({0}, {1})".format(len(i), i[0]), end=" ")
