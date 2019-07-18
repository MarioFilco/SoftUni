price_whiskey = float(input())
beer = float(input())
wine = float(input())
grappa = float(input())
whiskey = float(input())

price_grappa = price_whiskey / 2
price_wine = price_grappa * (1 - 0.40)
price_beer = price_grappa * (1 - 0.80)

money = (price_grappa * grappa) + (price_wine * wine) + (price_beer * beer) + (price_whiskey * whiskey)
print(f"{money:.2f}")
