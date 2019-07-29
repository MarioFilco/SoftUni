import operator
n_1 = int(input())
n_2 = int(input())
symbol = input()

allowed_operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}

if symbol == "/" and n_2 == 0 or symbol == "%" and n_2 == 0:
    print(f"Cannot divide {n_1} by zero")
elif symbol == "/":
    print(f"{n_1} / {n_2} = {(n_1 / n_2):.2f}")
elif symbol == "%":
    result = n_1 % n_2
    print(f"{n_1} % {n_2} = {result}")
elif symbol == "+" or symbol == "-" or symbol == "*":
    result = allowed_operators[symbol](n_1, n_2)
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{n_1} {symbol} {n_2} = {result} - {even_odd}")
