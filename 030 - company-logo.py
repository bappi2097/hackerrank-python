logo=list(input())
logo.sort()
dic = dict()
for i in logo:
    if i in dic.keys():
        dic[i]+=1
    else:
        dic[i]=1
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
j=0
for i in dic:
    j+=1
    print(i[0], i[1])
    if j>2:
        break
