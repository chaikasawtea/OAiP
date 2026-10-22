colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "black": (0, 0, 0),
}

c1 = colors["red"]
c2 = colors["green"]
mixed = tuple((a+b) // 2 for a, b in zip(c1,c2))
print(f"Смесь red и green: {mixed}")

color_to_invert = colors["blue"]
inverted = tuple(255 - c for c in color_to_invert)
print(f"Инверсия blue: {inverted}")