math_students = {"Alice", "Bob", "Charlie", "David"}
physics_students = {"Bob", "David", "Eve", "Frank"}
cs_students = {"Alice", "Charlie", "Eve", "Grace"}

all_three = math_students & physics_students & cs_students
print(f"Все три курса: {all_three}")

multi_course = (math_students & physics_students) | (math_students & cs_students) | (physics_students & cs_students)
all_students = math_students | physics_students | cs_students
only_one = all_students - multi_course
print(f"Только один курс: {only_one}")

math_not_physics = math_students - physics_students
print(f"Математика но не физика: {math_not_physics}")
print(f"Всего студентов: {len(all_students)}")