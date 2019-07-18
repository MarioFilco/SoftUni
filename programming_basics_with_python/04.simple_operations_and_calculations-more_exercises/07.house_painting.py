x = float(input())
y = float(input())
h = float(input())

red = ((x * h / 2) * 2) + ((x * y) * 2)
door_windows = (1.2 * 2) + (1.5 * 1.5 * 2)
green = (x * x * 2) + (x * y * 2) - door_windows
red_paint = red / 4.30
green_paint = green / 3.4
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
