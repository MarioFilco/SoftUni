trip_price = float(input())
num_puzzle = int(input())
num_speaking_doll = int(input())
num_teddy_bear = int(input())
num_minion = int(input())
num_truck = int(input())

discount = 0
puzzle = 2.60
speaking_doll = 3.00
teddy_bear = 4.10
minion = 8.20
truck = 2.00

num_all_toys = num_puzzle + num_speaking_doll + num_teddy_bear + num_minion + num_truck
if num_all_toys >= 50:
    discount = 25.00

money = (num_puzzle * puzzle) + \
        (num_speaking_doll * speaking_doll) + \
        (num_teddy_bear * teddy_bear) + \
        (num_minion * minion) + \
        (num_truck * truck)

money = money * (1 - (discount / 100))
profit = money * (1 - 0.10)

if profit >= trip_price:
    print(f"Yes! {profit - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - profit:.2f} lv needed.")
