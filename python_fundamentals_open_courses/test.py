#################
import re

s = '1-5,7,9,10-13'

r = [
    eval('[' + re.sub('(\d+)-(\d+)', r'*range(\1, \2+1)', s) + ']')
]
print(r)
#################
print((lambda t: t == t[::-1])(input().lower()))
###########
print("".join(map(lambda x: "Happy birthday to " + ("you " if x != 2 else f"dear {input()} "), range(4))))
###########

from math import sqrt

fib = lambda x: int(((1 + sqrt(5))**x - (1 - sqrt(5))**x) / (2**x * sqrt(5)))
print(fib(10))

fib = lambda x: list(map(lambda y: int(((1 + sqrt(5)) ** y - (1 - sqrt(5)) ** y) / (2 ** y * sqrt(5))), range(1, x+1)))
print(fib(100))
#################

fact = lambda x: 1 if x <= 1 else x * fact(x-1)
print(fact(4))

fact = lambda x: x and x * fact(x - 1) or 1
print(fact(10))

fact = lambda x: 1 if x == 0 else x * fact(x-1)
print(fact(10))

fact = lambda n: [1, 0][n > 1] or fact(n - 1) * n
print(fact(4))

from functools import reduce

fact = lambda x: reduce(lambda a, b: a*b, range(1, x+1))
print(fact(4))

from math import factorial

fact = lambda x: factorial(x)
print(fact(10))

from operator import mul

fact = lambda x: reduce(mul, range(1, x+1))
print(fact(10))


###################