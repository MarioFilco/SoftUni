age = int(input())
washing_machine = float(input())
price_toy = int(input())

brother_spend = 0
money_gift = 10
toys = 0
money = 0

for a in range(1, age + 1):
    if a % 2 != 0:
        toys += 1
    else:
        money += money_gift
        money_gift += 10
        brother_spend += 1


saved_money_toys = money - brother_spend + ( price_toy * toys)

if saved_money_toys >= washing_machine:
    print(f"Yes! {(saved_money_toys - washing_machine):.2f}")
else:
    print(f"No! {abs((saved_money_toys - washing_machine)):.2f}")
