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