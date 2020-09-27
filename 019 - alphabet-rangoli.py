def print_rangoli(size):
    for i in range(1, size+1):
        m=list("-"*(((size-1)*4)+1))
        for j in range(1, i+1):
            m[(2*(size-j))]=chr(ord("a")+size+j-i-1)
            m[(-2*(size-j)-1)]=chr(ord("a")+size+j-i-1)
        print("".join(m))
    for i in range(size-1, 0, -1):
        m=list("-"*(((size-1)*4)+1))
        for j in range(1, i+1):
            m[(2*(size-j))]=chr(ord("a")+size+j-i-1)
            m[(-2*(size-j)-1)]=chr(ord("a")+size+j-i-1)
        print("".join(m))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)