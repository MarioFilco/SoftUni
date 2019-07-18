square_meters = float(input())

price_per_meter = 7.61

sum_ = square_meters * price_per_meter
discount = sum_ * 0.18

print(f"The final price is: {sum_ - discount:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")
