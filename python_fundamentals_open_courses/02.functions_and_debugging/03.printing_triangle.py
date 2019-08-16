def print_col(col):
    print(f"{col} ", end='')


def print_row():
    print()


def draw(n):
    for row in range(1, n+1):
        for col in range(1, row+1):
            print_col(col)
        print_row()
    for row in range(n, 1, -1):
        for col in range(1, row):
            print_col(col)
        print_row()


def input_num():
    number = int(input())
    draw(number)


input_num()