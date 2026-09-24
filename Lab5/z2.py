a, b, c = map(int, input("Введите три целых числа через пробел: ").split())
ab = a * b
bc = b * c
ca = c * a

a4 = a ** 4
remainder = b % c 
division = c // a

result1 = a4
result2 = remainder 
result3 = division

print("a * b =", ab)
print("b * c =", bc)
print("c * a =", ca)

print("a ** 4 =", result1)
print("b % c =", result2)
print("c // a=", result3)

print("Сумма результатов пункта 5 =", result1 + result2 + result3)
 
