def minion_game(string):
    # your code goes here
    mp = {"Stuart": 0, "Kevin": 0}
    size = len(string)
    for i in range(size):
        s = string[i]
        if isvowel(s):
            mp["Kevin"] += size - i
        else:
            mp["Stuart"] += size - i

    if mp["Stuart"] > mp["Kevin"]:
        print("Stuart", mp["Stuart"])
    elif mp["Stuart"] < mp["Kevin"]:
        print("Kevin", mp["Kevin"])
    else:
        print("Draw")


def isvowel(s):
    return True if s[0] in ['A', 'E', 'I', 'O', 'U'] else False


if __name__ == '__main__':
    s = input()
    minion_game(s)