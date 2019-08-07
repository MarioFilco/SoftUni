number = int(input())

for i in range(1, len(str(number)) + 1):
    last_number = number % 10
    number = number // 10
    if last_number == 0:
        print('ZERO')
    else:
        for j in range(1, last_number + 1):
            print(chr(last_number + 33), end='')
        print()
