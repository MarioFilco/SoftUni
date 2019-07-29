budget = float(input())
season = input()

destination = None
room = None
discount = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        discount = 0.30
        room = "Camp"
    elif season == "winter":
        discount = 0.70
        room = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        discount = 0.40
        room = "Camp"
    elif season == "winter":
        discount = 0.80
        room = "Hotel"
else:
    destination = "Europe"
    discount = 0.90
    room = "Hotel"

cost = budget * discount
print(f"Somewhere in {destination}")
print(f"{room} - {cost:.2f}")
