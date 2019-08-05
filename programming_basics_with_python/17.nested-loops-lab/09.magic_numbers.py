from itertools import product
from functools import reduce
num = int(input())
mul = 0

for i in product(range(1, 10), repeat=6):
    mul = reduce((lambda x, y: x * y), i)
    # mul = i[0] * i[1] * i[2] * i[3] * i[4] * i[5]
    if mul == num:
        for y in i:
            print(y, end='')
        print(end=' ')
    mul = 1
