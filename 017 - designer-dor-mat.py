# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
n = int(n)
m = int(m)
lmt = int((n - 1) / 2)
symb = ".|."
for k in range(1, n, 2):
    print((symb * (k)).center(m, "-"))

print("WELCOME".center(m, "-"))

for k in range(n - 2, 0, -2):
    print((symb * (k)).center(m, "-"))

