n = int(input("Введите число: "))
s = 0
for i in range(1, n + 1):
    s += i
print("Вывод: ", s, "(", end="")
for i in range(1, n + 1):
    print(i, end="")
    if i < n:
        print("+", end="")
print(")")
