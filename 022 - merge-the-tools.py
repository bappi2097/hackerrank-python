def merge_the_tools(string, k):
    lst = list()
    for i in range(len(string) // k):
        lst.append(string[i * k:(i + 1) * k])
    for i in lst:
        s = dict()
        for j in i:
            s[j] = 0
        for k, v in s.items():
            print(k, end="")
        print("")


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)