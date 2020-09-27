def print_formatted(number):
    ln=len("{0:b}".format(number))+1
    for i in range(number):
        deci="{0}".format(i+1).rjust(ln-1)
        octa="{0:o}".format(i+1).rjust(ln)
        hexa="{0:x}".format(i+1).rjust(ln).upper()
        bina="{0:b}".format(i+1).rjust(ln)
        print(deci+octa+hexa+bina)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)