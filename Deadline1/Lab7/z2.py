password = input("Придумайте пароль: ")
confirm = input("Подтвердите пароль: ")

if password != confirm:
    print("Пароли не совпадают!")
else:
    login = input("Авторизуйтесь. Введите пароль: ")
    if login == password:
        print("Access")
    else:
        print("Denied")