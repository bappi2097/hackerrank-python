def minion_game(string):
    lnt = len(string)
    sub_strings = (lnt*(lnt+1))//2
    kevin = 0
    for i in range(lnt):
        if isvowel(string[i]):
            kevin += (lnt-i)
    if kevin > sub_strings-kevin:
        print("Kevin", kevin)
    elif kevin < sub_strings-kevin:
        print("Stuart", sub_strings-kevin)
    else:
        print("Draw")

def isvowel(s):
    return True if s in ["A", "E", "I", "O", "u"] else False

if __name__ == '__main__':
    s = input()
    minion_game(s)