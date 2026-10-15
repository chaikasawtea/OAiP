p = {"Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}}
best_name = ""
max_sold = 0
for name, info in p.items():
    if info["sold"] > max_sold:
        max_sold = info["sold"]
        best_name = name
print(f"Самый продаваемый: {best_name}")

total_rev = 0
for name, info in p.items():
    total_rev += info["price"] * info["sold"]
print(f"Общая выручка: {total_rev}")

top_name = ""
max_rev = 0
for name, info in p.items():
    rev = info["price"] * info["sold"]
    if rev > max_rev:
        max_rev = rev
        top_name = name
print(f"Наибольшая выручка у: {top_name}")