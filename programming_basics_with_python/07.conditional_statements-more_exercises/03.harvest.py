from math import ceil

x = int(input())
y = float(input())
z = int(input())
num = int(input())

kilograms_grapes = (x * y) * (40 / 100)
liters_wine = kilograms_grapes / 2.50
diff_liters_wine = z - liters_wine
if diff_liters_wine > 0:
    print(f"It will be a tough winter! More {int(diff_liters_wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {int(abs(liters_wine))} liters.")
    diff = abs(diff_liters_wine)
    print(f"{ceil(diff)} liters left -> {ceil(diff / num)} liters per person.")
