prime_num_sum = 0
non_prime_num_sum = 0
while True:
    num = input()
    if num == 'stop':
        print(f'Sum of all prime numbers is: {prime_num_sum}')
        print(f'Sum of all non prime numbers is: {non_prime_num_sum}')
        break
    num = int(num)
    is_prime_num = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            is_prime_num = True
    if num < 0:
        print(f'Number is negative.')
        is_prime_num = False
    if is_prime_num:
        prime_num_sum += num
    elif not is_prime_num and num >= 0:
        non_prime_num_sum += num