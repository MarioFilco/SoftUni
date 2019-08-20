from itertools import combinations
from operator import mul
from functools import reduce
n = [4, 3, 5]
k = 2
for x in combinations(n, k):
  print(list(x))
  print(reduce(lambda a,b: a*b,list(x)))

print((list(x)) for x in combinations(n, k))


fact = lambda x: 1 if x <= 1 else x * fact(x-1)
print(fact(10))

fact = lambda x: x and x * fact(x - 1) or 1
print(fact(10))

fact = lambda x: 1 if x == 0 else x * fact(x-1)
print(fact(10))

fact = lambda n: [1, 0][n > 1] or fact(n - 1) * n
print(fact(10))
