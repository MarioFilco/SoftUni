def print_range(num):
    print(num)


def _range(start, end, step):
    for n in range(start, end, step):
        print_range(n)


def input_range():
    start_number = int(input())
    end_number = int(input())
    step = int(input())
    _range(start_number, end_number, step)


input_range()
