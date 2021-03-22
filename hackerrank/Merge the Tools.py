import textwrap
def merge_the_tools(string, k):
    sub_strings = textwrap.wrap(string, k)
    for i in sub_strings:
        mp = dict()
        for j in list(i):
            mp[j] = True
        for index, value in mp.items():
            print(index, end="")
        print("")

if __name__ == '__main__':
    # string, k = input(), int(input())
    string = "AABCAAADA"
    k = 3
    merge_the_tools(string, k)