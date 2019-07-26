days = int(input())
room_type = input()
rating = input()

days -= 1
discount = 0
room = 18.00
apartment = 25.00
president_apartment = 35.00

if room_type == "room for one person":
    if days < 10:
        pass
    elif 10 <= days <= 15:
        pass
    elif days > 15:
        pass
    cost = days * room * (1 - discount)
elif room_type == "apartment":
    if days < 10:
        discount = 0.30
    elif 10 <= days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.50
    cost = days * apartment * (1 - discount)
elif room_type == "president apartment":
    if days < 10:
        discount = 0.10
    elif 10 <= days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.20
    cost = days * president_apartment * (1 - discount)

if rating == "positive":
    cost += cost * 0.25
elif rating == "negative":
    cost -= cost * 0.10

print(f"{cost:.2f}")
