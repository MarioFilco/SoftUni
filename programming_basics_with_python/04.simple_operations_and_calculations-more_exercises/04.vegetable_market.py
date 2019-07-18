price_vegetables = float(input())
price_fruit = float(input())
total_vegetables = int(input())
total_fruit = int(input())

money = ((price_vegetables * total_vegetables) + (price_fruit * total_fruit)) / 1.94

print(f"{money:.2f}")
