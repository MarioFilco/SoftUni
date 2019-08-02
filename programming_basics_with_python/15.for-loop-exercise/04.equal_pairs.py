from functools import reduce


def sum_x_y(x, y):
    return x + y


n = int(input())

sum_list = []
for _ in range(n):
    sum_num = 0
    num_1 = int(input())
    num_2 = int(input())
    sum_num = num_1 + num_2
    sum_list.append(sum_num)
    margin = list(map(lambda x: x+1, sum_list))
if max(sum_list) == min(sum_list):
    print(f"Yes, value={max(sum_list)}")
else:
    print(f"No, maxdiff={max(sum_list) - min(sum_list)}")


# n = int(input())
# value = 0
# value_diff = 0
# sum_num_after = 0
# sum_num = 0
# for n in range(1, n + 1):
#     num_1 = int(input())
#     num_2 = int(input())
#     sum_num = num_1 + num_2
#     if n == 1:
#         sum_num_after = sum_num
#     if sum_num_after == sum_num:
#         value = sum_num_after
#     else:
#         value_diff_after = abs(sum_num_after - sum_num)
#         sum_num_after = sum_num
# if value == sum_num:
#     print(f"Yes, value:{value}")
# else:
#     print(f"No, maxdiff={value_diff_after}")
