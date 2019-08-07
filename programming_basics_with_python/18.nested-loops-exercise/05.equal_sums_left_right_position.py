num_1 = int(input())
num_2 = int(input())

for number in range(num_1, num_2 + 1):
    num = number
    right_nums_sum = 0
    left_nums_sum = 0
    middle_nums = 0
    right_nums_sum += num % 10
    num = num // 10
    right_nums_sum += num % 10
    num = num // 10
    middle_nums = num % 10
    num = num // 10
    left_nums_sum += num % 10
    num = num // 10
    left_nums_sum += num % 10
    num = num // 10
    if left_nums_sum == right_nums_sum:
        print(number, end=' ')
    else:
        if (left_nums_sum > right_nums_sum) and left_nums_sum == (right_nums_sum + middle_nums):
            print(number, end=' ')
        elif (left_nums_sum < right_nums_sum) and (left_nums_sum + middle_nums) == right_nums_sum:
            print(number, end=' ')