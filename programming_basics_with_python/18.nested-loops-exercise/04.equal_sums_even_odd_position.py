num_1 = int(input())
num_2 = int(input())

for n in range(num_1, num_2 + 1):
    odd_sum = 0
    even_sum = 0
    number = n
    for i in range(3):
        even_sum += n % 10
        n = n // 10
        odd_sum += n % 10
        n = n // 10
    if odd_sum == even_sum:
        print(number, end=' ')
