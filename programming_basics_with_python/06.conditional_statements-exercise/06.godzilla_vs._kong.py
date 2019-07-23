budget = float(input())
static = int(input())
price_clothing = float(input())

discount = 0
decor = budget * 0.10
if static > 150:
    discount = 0.10


cost = (static * price_clothing * (1 - discount)) + decor
diff = budget - cost
if diff >= 0:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {abs(diff):.2f} leva more.")
