product = input()

product_dict = {
    "fruit": ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"],
    "vegetable": ["tomato", "cucumber", "pepper", "carrot"]
}
food_in = False

for search_ in product_dict.items():
    if product in search_[1]:
        target = search_[0]
        food_in = True

if food_in:
    print(target)
else:
    print(f"unknown")
