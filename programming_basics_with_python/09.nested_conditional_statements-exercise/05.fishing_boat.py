budget = int(input())
season = input()
num_fisherman = int(input())

price_rent_ship = 0
if season == "Spring":
    price_rent_ship = 3000
elif season == "Summer" or season == "Autumn":
    price_rent_ship = 4200
elif season == "Winter":
    price_rent_ship = 2600

if num_fisherman <= 6:
    discount = 0.10
elif (num_fisherman > 7) and (num_fisherman <= 11):
    discount = 0.15
else:
    discount = 0.25
cost = price_rent_ship * (1 - discount)
if season != "Autumn" and num_fisherman % 2 == 0:
    cost *= (1 - 0.05)

diff = budget - cost
if diff >= 0:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff):.2f} leva.")
