from math import sqrt

fib_list = []
for n in range(1, 4000000 + 1):
    fib = int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))
    if fib % 2 == 0:
        fib_list.append(fib)
    if fib >= 4000000:
        break
print(sum(fib_list))

#

import sys

max_num = sys.maxsize
range_ = 20
for num in range(1, max_num):
    list_ = []
    for n in range(1, range_ + 1):
        if num % n == 0:
            list_.append(1)
        else:
            list_.append(0)
            break
    if 0 not in list_:
        print(num)
        break
