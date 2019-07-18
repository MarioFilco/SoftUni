days = int(input())
confectioners = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

cakes_price = 45.00
waffles_price = 5.80
pancakes_price = 3.20

sums = (cakes * cakes_price) + (waffles * waffles_price) + (pancakes * pancakes_price)
money = (sums * confectioners * days) * (1 - 0.125)
print(f"{money:.2f}")
