a = int(input())
b = int(input())
c = int(input())
d = int(input())

for a_b_1 in range(a, b + 1):
    for a_b_2 in range(a, b + 1):
        for c_d_1 in range(c, d + 1):
            for c_d_2 in range(c, d + 1):
                if (a_b_1 + c_d_2 == a_b_2 + c_d_1) and not (a_b_1 == a_b_2) and not (c_d_1 == c_d_2):
                    print(f'{a_b_1}{a_b_2}')
                    print(f'{c_d_1}{c_d_2}')
                    print()
