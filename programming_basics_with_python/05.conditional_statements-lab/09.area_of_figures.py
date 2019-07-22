from math import pi

figure = input()
area = None
if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
elif figure == "circle":
    radius = float(input())
    area = (radius ** 2) * pi
elif figure == "triangle":
    side_1 = float(input())
    h = float(input())
    area = (side_1 * h) / 2

result = round(area, 3)
print(f"{result:.3f}")
