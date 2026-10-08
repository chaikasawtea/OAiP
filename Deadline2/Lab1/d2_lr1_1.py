num = int(input("Введите положительное число: "))
sum_digits = 0
temp_num = num
while temp_num > 0:
    last_digit = temp_num % 10
    sum_digits += last_digit
    temp_num = temp_num // 10
print(f"Сумма цифр числа {num}: {sum_digits}")