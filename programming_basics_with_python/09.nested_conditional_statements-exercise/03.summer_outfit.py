degrees = int(input())
time_of_day = input()


weather = None
if 10 <= degrees <= 18:
    weather = "cool"
elif 18 < degrees <= 24:
    weather = "medium"
elif degrees >= 25:
    weather = "hot"

choice_dict = {
    "Morning": {
        "cool": ["Sweatshirt", "Sneakers"],
        "medium": ["Shirt", "Moccasins"],
        "hot": ["T-Shirt", "Sandals"]
    },
    "Afternoon": {
        "cool": ["Shirt", "Moccasins"],
        "medium": ["T-Shirt", "Sandals"],
        "hot": ["Swim Suit", "Barefoot"]
    },
    "Evening": {
        "cool": ["Shirt", "Moccasins"],
        "medium": ["Shirt", "Moccasins"],
        "hot": ["Shirt", "Moccasins"]
    }
}

outfit = choice_dict[time_of_day][weather][0]
shoes = choice_dict[time_of_day][weather][1]
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
