grades = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    grades.append([name, score])
low = grades[0][1]
sec = grades[0][1]
for i in grades:
    if i[1] < low:
        low = i[1]
    if i[1] > sec:
        sec = i[1]
for i in grades:
    if sec > i[1] > low:
        sec = i[1]
secGrades = []
for i in grades:
    if i[1] == sec:
        secGrades.append(i[0])
secGrades.sort()
for i in secGrades:
    print(i)
