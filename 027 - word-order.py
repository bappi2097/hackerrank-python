n = int(input())
dic={}
for i in range(0, n):
    temp=input()
    if temp in  dic.keys():
        dic[temp]+=1
    else:
        dic[temp]=1
print(len(list(dic.values())))
for  i in list(dic.values()):
    print(i, end = " ")
