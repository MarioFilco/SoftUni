degree_celsius = float(input())

if (degree_celsius >= 26.00) and (degree_celsius <= 35.00):
    print(f"Hot")
elif (degree_celsius >= 20.10) and (degree_celsius <= 25.90):
    print(f"Warm")
elif (degree_celsius >= 15.00) and (degree_celsius <= 20.00):
    print(f"Mild")
elif (degree_celsius >= 12.00) and (degree_celsius <= 14.90):
    print(f"Cool")
elif (degree_celsius >= 5.00) and (degree_celsius <= 11.90):
    print(f"Cold")
else:
    print(f"unknown")
