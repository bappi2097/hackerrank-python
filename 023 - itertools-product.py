from itertools import product
A=list(map(int, input().split()))
B=list(map(int, input().split()))
prdct=list(product(A,B))
for i in prdct:
    print(i, end=" ")
