if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sec = -101
    top = max(arr)
    for i in arr:
        if sec < i < top:
            sec = i
    print(sec)
