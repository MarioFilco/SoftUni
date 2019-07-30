month = input()
nights = int(input())


discount_studio = 0
discount_apartment = 0

if month == "May" or month == "October":
    studio = 50.00
    apartment = 65.00
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
elif month == "July" or month == "August":
    studio = 76.00
    apartment = 77.00
if nights > 7:
    if month == "May" or month == "October":
        discount_studio = 0.05
if nights > 14:
    if month == "May" or month == "October":
        discount_studio = 0.30
    elif month == "June" or month == "September":
        discount_studio = 0.20
    discount_apartment = 0.10

print(f"Apartment: {((apartment * (1 - discount_apartment)) * nights):.2f} lv.")
print(f"Studio: {((studio * (1 - discount_studio)) * nights):.2f} lv.")
