n = int(input())
p_1 = 0
p_2 = 0
p_3 = 0

for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        p_1 += 1
    if num % 3 == 0:
        p_2 += 1
    if num % 4 == 0:
        p_3 += 1

print(f"{(p_1 / n) * 100:.2f}%")
print(f"{(p_2 / n) * 100:.2f}%")
print(f"{(p_3 / n) * 100:.2f}%")
