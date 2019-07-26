x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x = float(input())
y = float(input())

is_in_x_border = ((x_1 == x) or (x_2 == x)) and y_1 <= y <= y_2
is_in_y_border = ((y_1 == y) or (y_2 == y)) and x_1 <= x <= x_2
if is_in_x_border or is_in_y_border:
    print(f"Border")
else:
    print(f"Inside / Outside")
