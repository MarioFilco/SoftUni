change = float(input())
change = round(change * 100)
coin = 200
total_coins = 0
while not change == 0:
    coins = change // coin
    change = change % coin
    coin = coin // 2
    if coin == 25:
        coin = 20
    total_coins += coins
print(total_coins)


# change = float(input())
#
# count = 0
# while change:
#     if change >= 2:
#         change -= 2
#     elif change >= 1:
#         change -= 1
#     elif change >= 0.50:
#         change -= 0.50
#     elif change >= 0.20:
#         change -= 0.20
#     elif change >= 0.10:
#         change -= 0.10
#     elif change >= 0.05:
#         change -= 0.05
#     elif change >= 0.02:
#         change -= 0.02
#     elif change >= 0.01:
#         change -= 0.01
#     change = round(change, 2)
#     count += 1
#
# print(f"{count}")
