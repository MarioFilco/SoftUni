number = int(input())
letter = int(input())

for num_1 in range(1, number + 1):
    for num_2 in range(1, number + 1):
        for letter_1 in range(97, 97 + letter):
            for letter_2 in range(97, 97 + letter):
                for num_3 in range(1, number + 1):
                    if num_3 > num_1 and num_3 > num_2:
                        print(f'{num_1}{num_2}{chr(letter_1)}{chr(letter_2)}{num_3}', end=' ')


# import itertools
# number = int(input())
# letter = int(input())
# letter_1 = map(chr, range(97, 97 + letter))
# letter_2 = map(chr, range(97, 97 + letter))
# ranges = [
#     range(1, number + 1),
#     range(1, number + 1),
#     letter_1,
#     letter_2,
#     range(1, number + 1),
#
# ]
#
# for num in itertools.product(*ranges):
#     if (int(num[4]) > int(num[0])) and (int(num[4]) > int(num[1])):
#         for n in num:
#             print(f'{n}', sep='', end='')
#         print(end=' ')
#
