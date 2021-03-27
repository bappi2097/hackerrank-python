def print_formatted(number):
    ln = len("{0:b}".format(number)) + 1
    for i in range(1, number+1):
        print("{0}".format(i).rjust(ln-1)+"{0:o}".format(i).rjust(ln)+"{0:x}".format(i).rjust(ln).upper()+"{0:b}".format(i).rjust(ln))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)