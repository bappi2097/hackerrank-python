def swap_case(s):
    list_s = list(s)
    for i in range(len(list_s)):
        if list_s[i].isalpha():
            if list_s[i].isupper():
                list_s[i] = list_s[i].lower()
            else:
                list_s[i] = list_s[i].upper()
    return "".join(list_s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
