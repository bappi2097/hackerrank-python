students = {}
for _ in range(int(input())):
    name, *line = input().split()
    scores = list(map(float, line))
    students[name] = scores
query_name = input()
sums = sum(students[query_name])
print("{:.2f}".format(sums/3, 2))

