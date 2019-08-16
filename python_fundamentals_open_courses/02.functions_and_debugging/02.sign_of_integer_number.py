def sing_of_number(n):
    if n > 0:
        print(f"The number {n} is positive.")
    elif n < 0:
        print(f"The number {n} is negative.")
    else:
        print("The number 0 is zero.")


def input_number():
    num = int(input())
    sing_of_number(num)


input_number()
