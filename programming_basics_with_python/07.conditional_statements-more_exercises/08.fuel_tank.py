fuel_type = input()
liters = int(input())

if fuel_type in ["Diesel", "Gasoline", "Gas"]:
    if liters >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print(f"Invalid fuel!")
