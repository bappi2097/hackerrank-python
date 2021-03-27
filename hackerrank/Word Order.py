dict = {}
for i in range(int(input())):
    s = input()
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1
print(len(dict))
for i in dict:
    print(dict[i], end=" ")
