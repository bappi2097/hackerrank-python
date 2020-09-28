from itertools import combinations
s,r=input().split()
com=list()
fin=[]
for i in range(1, int(r)+1):
    lst=[]
    com=list(combinations(sorted(s), int(i)))
    for i in com:
        lst.append("".join(i))
    lst.sort()
    fin+=lst
for i in fin:
    print(i)
