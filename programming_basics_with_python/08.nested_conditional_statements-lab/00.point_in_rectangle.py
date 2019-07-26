x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x = float(input())
y = float(input())

is_in_x = (x >= x_1) and (x <= x_2)
is_in_y = (y >= y_1) and (y <= y_2)

if is_in_x and is_in_y:
    print(f"Inside")
else:
    print(f"Outside")
