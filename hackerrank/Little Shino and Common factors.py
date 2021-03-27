import math
a, b = map(int, input().split())
low = a if a <= b else b
high = b if b >= a else a
if a == 1 or b == 1:
    print(1)
else:
    arr = []
    count = 0
    sqrtLow = int(math.sqrt(low+1))
    for i in range(1, sqrtLow+1):
        if low % i == 0:
            arr.append(i)
            arr.append(low//i)
    for i in arr:
        if high % i == 0:
            count += 1
    print(count)