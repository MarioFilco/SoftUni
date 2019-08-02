n = int(input())
value = 0
value_diff = 0
sum_num_after = 0
sum_num = 0
for n in range(1, n + 1):
    num_1 = int(input())
    num_2 = int(input())
    sum_num = num_1 + num_2
    if n == 1:
        sum_num_after = sum_num
    if sum_num_after == sum_num:
        value = sum_num_after
    else:
        value_diff_after = abs(sum_num_after - sum_num)
        sum_num_after = sum_num
if value == sum_num:
    print(f"Yes, value={value}")
else:
    print(f"No, maxdiff={value_diff_after}")