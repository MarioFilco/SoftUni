from math import floor, ceil

days = int(input())
food = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
turtle_food_day = float(input())

food_per_day = dog_food_day + cat_food_day + (turtle_food_day / 1000)
diff = food - (food_per_day * days)

if diff >= 0:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(abs(diff))} more kilos of food are needed.")
