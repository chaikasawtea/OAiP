d = {}
while True:
    s = input("Введите текст (или нажмите Ввод для выхода):")
    if s == "":
        break
    for c in ".,!?;:-":
        s = s.replace(c,"")
    for w in s.lower().split():
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
print("Стастиска слов: ", d)