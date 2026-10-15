n = int(input("Сколько чисел вывести: "))
numbers = []

for i in range(1, n + 1):
    num = int(input("Введите число " + str(i) + ": "))
    numbers.append(num)

av = sum(numbers) / n
count = 0

for num in numbers:
    if num > av:
        count += 1

print("Результат: ")
print("Максимальное: ", max(numbers))
print("Минимальное: ", min(numbers))
print("Среднее: ", av)
print("Чисел больше среднего: ", count)