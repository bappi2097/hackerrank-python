def print_rangoli(size):
    lent = (((size * 2) - 1) * 2) - 1
    s = "abcdefghijklmnopqrstuvwxyz"
    for i in range(size):
        string = s[size - i - 1:size]
        string = "-".join(list(string[:0:-1] + string))
        print(string.center(lent, "-"))
    for i in range(size - 2, -1, -1):
        string = s[size - i - 1:size]
        string = "-".join(list(string[:0:-1] + string))
        print(string.center(lent, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)