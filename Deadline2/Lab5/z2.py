student = [
    ("Ульяна", 19, 4.5),
    ("Диас", 18, 4.2),
    ("Денис", 19, 4.8),
    ("Марина", 18, 3.9),
    ("Саша", 18, 3.2),
]

print("Студенты старше 18: ")
for name,age,score in student:
    if age > 18:
        print(f"- {name} ({age}),средний балл: {score}")
best_student = max(student, key=lambda s: s[2])
print(f"\nЛучший студент: {best_student[0]}, средний балл: {best_student[2]}")

sorted_student = sorted(student, key=lambda s: s[0])
print("\nОтсортированные по имени стунденты: ")
for s in sorted_student:
    print(s)


