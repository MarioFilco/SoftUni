number = int(input())

for num in range(1110, 9999 + 1):
    current_num = num
    n = current_num % 10
    if n == 0:
        continue
    if number % n == 0:
        current_num = current_num // 10
        n = current_num % 10
        if n == 0:
            continue
        if number % n == 0:
            current_num = current_num // 10
            n = current_num % 10
            if n == 0:
                continue
            if number % n == 0:
                current_num = current_num // 10
                n = current_num % 10
                if n == 0:
                    continue
                if number % n == 0:
                    current_num = current_num // 10
                    n = current_num % 10
                    print(num, end=' ')
