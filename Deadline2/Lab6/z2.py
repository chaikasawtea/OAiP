def simple_calculator(num1,num2,operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите оператор (+,-,*,/): ")

result = simple_calculator(a, b, op)
print(f"Результат: {result}")
