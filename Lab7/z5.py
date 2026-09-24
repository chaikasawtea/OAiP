import math

expr = input("Введите выражение (например, 5 + 3): ").split()
num1 = float(expr[0])
operator = expr[1]
num2 = float(expr[2])

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '%':
    print(num1 % num2)
elif operator == '//':
    print(num1 // num2)
elif operator == '**':
    print(num1 ** num2)
elif operator == '%%':
    print(num2 / 100 * num1) # число 2 процентов от числа 1
elif operator == '/**':
    print(math.sqrt(num1)) # корень числа 1 (num2 игнорируется, но вводится по условию)
else:
    print("Неизвестный оператор")