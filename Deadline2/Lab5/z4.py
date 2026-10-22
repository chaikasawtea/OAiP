text = input("Введите текст: ")
clean_text = text.lower().replace('.','').replace(',','')
words = set(clean_text.split())

print(f"\nУникальные слова: {len(words)}")
long_words = {word for word in words if len(word) > 5}
print(f"Длинные слова: {long_words}")

has_keywords = "python" in words or "programming"
print(f"найдены ключевые слова: {has_keywords}")