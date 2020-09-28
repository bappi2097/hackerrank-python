from itertools import permutations
s, r=input().split()
per=list(permutations(list(s),int(r)))
lst=[]
for i in per:
    lst.append("".join(i))
lst.sort()
for i in lst:
    print(i)
