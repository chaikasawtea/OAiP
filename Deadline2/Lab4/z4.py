temp = [15,18,12,20,16,14,19,17,13,21,15,16,18,20]
print(f"Температуры:{temp}")
print(f"Максимальная:{max(temp)}°C")
print(f"Минимальная:{min(temp)}°C")

avg_temp = sum(temp) / len(temp)
print(f"Средняя:{round(avg_temp, 1)}°C")

day_ab = sum(temp) / len(temp)
print(f"Дней выше средней:{day_ab}")
print(f"Отсортированный список:{sorted(temp)}")

fah = [round(c * 9/5 + 32 , 1) for c in temp]
print(f"В Фаренгейтах: {fah}")