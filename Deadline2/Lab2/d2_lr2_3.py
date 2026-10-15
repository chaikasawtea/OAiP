text = input("Введите текст: ")

let = 0
cif = 0
pun = 0
spaces = 0

for c in text:
    if c.isalpha():
        let += 1
    elif c.isdigit():
        cif += 1
    elif c in ".,!?;:":
        pun += 1
    elif c == " ":
        spaces += 1
print("букв = ", let)
print("цифр = ", cif)
print("знаков препинания = ", pun)
print("пробелов = ", spaces)