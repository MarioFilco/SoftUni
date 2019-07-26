fuel_type = input()
liters_quality = float(input())
discount_card = input()

discount = 0
price = {
    "Gasoline": 2.22,
    "Diesel": 2.33,
    "Gas": 0.93
}

if liters_quality > 25:
    discount += 0.10
elif (liters_quality >= 20) and (liters_quality <= 25):
    discount += 0.08
if discount_card == "Yes":
    if fuel_type == "Gasoline":
        price_discount = 0.18
    elif fuel_type == "Diesel":
        price_discount = 0.12
    elif fuel_type == "Gas":
        price_discount = 0.08
else:
    price_discount = 0

cost = (liters_quality * (price[fuel_type] - price_discount)) * (1 - discount)
print(f"{cost:.2f} lv.")
