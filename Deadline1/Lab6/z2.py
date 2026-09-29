text = input("Введите текст: ")
replace_str = input("Введите строку1 и строку2 через пробел: ").split()
new_text = text.replace(replace_str[0], replace_str[1])
print(new_text)