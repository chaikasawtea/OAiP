def power(number, degree=2):
    return number ** degree
num = float(input("Введите число: "))
deg_input = input("Введите степень (или нажмите Ввод для возведения в квадрат): ")

if deg_input == "":
    print(power(num))
else:
    print(power(num, int(deg_input)))