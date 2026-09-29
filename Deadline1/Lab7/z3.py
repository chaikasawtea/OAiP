text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

if word in text:
    count = text.count(word)
    print(f"Слово найдено! Количество вхождений: {count}")
else:
    print("Слово не найдено.")