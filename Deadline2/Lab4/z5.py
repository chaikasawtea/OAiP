import string 
from collections import Counter

text = input("Введите текст: ")
clean_text = text.translate(str.maketrans('','',string.punctuation))
word = clean_text.lower().split()

long = max(word, key=len)
short = min(word, key=len)

avg_len = sum(len(w) for w in word) / len(word)
top_5 = Counter(word).most_common(5)

print(f"Самое длинное слово: {long}")
print(f"Самое короткое: {short}")
print(f"Средняя длина: {round(avg_len, 1)}")
print(f"Топ-5 слов: {top_5}")