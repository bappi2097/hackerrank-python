if __name__ == '__main__':
    s = input()
    s = list(s)
    dict1 = dict({
        "alnum":False,
        "alpha":False,
        "digit":False,
        "lower":False,
        "upper":False,
    })
    for i in s:
        if i.isalnum():
            dict1["alnum"]=True
        if i.isalpha():
            dict1["alpha"]=True
        if i.isdigit():
            dict1["digit"]=True
        if i.islower():
            dict1["lower"]=True
        if i.isupper():
            dict1["upper"]=True
    for i in dict1.values():
        print(i)