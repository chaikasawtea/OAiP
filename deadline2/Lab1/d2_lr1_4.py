from random import randint 

random_num = randint(1, 100)
print("Я загадал число от 1 до 100. Угадай :)")

while True:
    guess = int(input("Введи число: "))
    
    if guess == random_num :
        print("Угадал :(")
        break
    elif guess > random_num:
        print("Меньше:)")
    else:
        print("Больше >:(")
    