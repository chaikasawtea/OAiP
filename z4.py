numbers = []

for i in range(5):
    number = int(input("Введите число: "))
    numbers.append(number)
    
print("Минимальное:", min(numbers))
print("Максимальное:", max(numbers))
