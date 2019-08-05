n = int(input())
p_1 = 0
p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0
for _ in range(n):
    num = int(input())
    if num < 200:
        p_1 += 1
    elif 200 <= num <= 399:
        p_2 += 1
    elif 400 <= num <= 599:
        p_3 += 1
    elif 600 <= num <= 799:
        p_4 += 1
    elif num >= 800:
        p_5 += 1
print(f"{(p_1 / n) * 100:.2f}%")
print(f"{(p_2 / n) * 100:.2f}%")
print(f"{(p_3 / n) * 100:.2f}%")
print(f"{(p_4 / n) * 100:.2f}%")
print(f"{(p_5 / n) * 100:.2f}%")
