scores = [
    [85, 90, 78, 92],
    [88, 75, 82, 91],
    [92, 88, 85, 89]
]

averanges = []
for student in scores:
    avg = sum(student) / len(student)
    averanges.append(avg)

print(f"Средний балл каждого студента: {averanges}")

for  i in range(len(scores[0])):
    total = 0
    for student in scores:
        total += student[i]
        print(f"средний балл {i+1}: {total / len(scores)}")

best = averanges.index(max(averanges))
print(f"Лучший студент: {best + 1}")

for i in range(len(averanges)):
    if averanges[i] > 85:

        print(f"Студенты с баллом выше 85: {i+1}")
