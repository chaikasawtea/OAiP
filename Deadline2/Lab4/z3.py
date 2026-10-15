t = []
while True:
    print("\n1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - отметить выполненной (удалить)")
    print("4 - Выйти")
    c = input("Выберите действие: ")
    
    if c == '1':
        for i, task in enumerate(t):
            print(f"{i+1}. {task}")
    elif c == '2':
        s = input("Введите описание задачи: ")
        t.append(s)
    elif c == '3':
        for i,task in enumerate(t):
            print(f"{i+1}. {task}")
        if len(t) > 0:
            n = int(input("Какую задачу выполнили? "))
            if 0 <= n < len(t):
                rem = t.pop(n)
                print(f'Задача "{rem}" удалена')
            else:
                print("Неверный номер")
        else:
            print("Список задач пуст")
    elif c == '4':
        exit()