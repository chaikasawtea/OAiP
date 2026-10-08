count = 0
print("Вводите числа (для завершения введите 0):")
while True:
    num = float(input())
    if num == 0:
        break
count += 1
print(f"Количество введенных чисел до нуля: {count}")
