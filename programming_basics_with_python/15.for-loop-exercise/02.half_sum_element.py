n = int(input())
number_list = []
for _ in range(n):
    num = int(input())
    number_list.append(num)
max_num = max(number_list)
sum_list_without_max_num = sum(number_list) - max_num
if sum_list_without_max_num == max_num:
    print(f"Yes")
    print(f"Sum = {max_num}")
else:
    print(f"No")
    print(f"Diff = {abs(sum_list_without_max_num - max_num)}")

# n = int(input())
# sum_num = 0
# max_num = 0
# for n in range(1, n + 1):
#     num = int(input())
#     if max_num < num:
#         max_num = num
#     sum_num += num
# result = sum_num - max_num
# if result == max_num:
#     print("Yes")
#     print(f"Sum = {result}")
# else:
#     print("No")
#     print(f"Diff = {abs(max_num - result)}")
