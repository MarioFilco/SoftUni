number = int(input())

bonus = 0

if number > 1000:
    bonus = number * 0.10
elif number > 100:
    bonus = number * 0.20
elif number <= 100:
    bonus = 5
if number % 2 == 0:
    bonus = bonus + 1
if number % 10 == 5:
    bonus = bonus + 2

print(f"{bonus:g}")
print(f"{number + bonus:g}")
