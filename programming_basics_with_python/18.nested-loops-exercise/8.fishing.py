limit_fishes = int(input())
money = 0
sum_per_fish = 0
fish = 0
while True:
    money_per_fish = 0
    sum_per_fish = 0
    name_fish = input()
    if name_fish == 'Stop':
        break
    kilograms_fish = float(input())
    fish += 1

    for i in name_fish:
        money_per_fish += ord(i)
    sum_per_fish = money_per_fish / kilograms_fish
    if fish % 3 == 0:
        money += sum_per_fish
    else:
        money -= sum_per_fish
    if fish == limit_fishes:
        print(f'Lyubo fulfilled the quota!')
        break


if money >= 0:
    print(f'Lyubo\'s profit from {fish} fishes is {money:.2f} leva.')
else:
    print(f'Lyubo lost {abs(money):.2f} leva today.')
