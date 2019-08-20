
fact = lambda x: 1 if x <= 1 else x * fact(x-1)
print(fact(10))

fact = lambda x: x and x * fact(x - 1) or 1
print(fact(10))

fact = lambda x: 1 if x == 0 else x * fact(x-1)
print(fact(10))

fact = lambda n: [1, 0][n > 1] or fact(n - 1) * n
print(fact(10))
