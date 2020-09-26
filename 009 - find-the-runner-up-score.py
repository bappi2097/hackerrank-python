if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    top = max(arr)
    sec = min(arr)
    for i in arr:
        if i>sec and i<top:
            sec=i
    print(sec) 