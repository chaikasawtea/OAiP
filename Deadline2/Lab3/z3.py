pb = {'Денис': '111', 'Ульяна': '222', 'Юра': '333'}
while True:
    print("\n1 - Показать, 2 - Добавить, 3 - Удалить, 4 - Выйти")
    act = input("Введите номер действия: ")
    
    if act == '1':
        for n, t in pb.items():
            print(f"{n}: {t}")
    
    elif act == '2':
        n = input("Введите имя: ")
        if n in pb:
            print("Контакт с подобным именем уже существует")
        else:
            t = input("Введите телефон: ")
            pb[n] = t
    elif act == '3':
        n = input ("Введите имя: ")
        if n in pb:
            del pb[n]
        else:
            print("Такого контакта не существует")
    elif act == '4':
        exit()
        
    