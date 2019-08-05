from itertools import product

n = int(input())

count = 0
for num in product(range(0, n+1), repeat=5):
    if sum(num) == n:
        count += 1
print(count)

# number = int(input())
# amount = 0
# current_sum = 0
#
# for x_1 in range(number + 1):
#     for x_2 in range(number + 1):
#         for x_3 in range(number + 1):
#             for x_4 in range(number + 1):
#                 for x_5 in range(number + 1):
#                     current_sum = x_1 + x_2 + x_3 + x_4 + x_5
#                     if current_sum == number:
#                         current_sum = 0
#                         amount += 1
#                         break
# print(amount)
