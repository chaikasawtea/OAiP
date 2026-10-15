g = []
print("Введите 5 оценок: ")
for i in range(5):
    o = int(input("Оценка: "))
    g.append(o)
print("Текущие оценки: ", g)

g.pop(0)
g.pop()

sr = sum(g) / len(g)
print("Средний балл: ", sr)
print("Итоговые оценки: ", g)