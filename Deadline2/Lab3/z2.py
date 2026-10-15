s = input("Введите текст: ")
d={}
for c in s.lower():
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
        
print(d)