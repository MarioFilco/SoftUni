city = input()
sales = float(input())

cities = ["Sofia", "Varna", "Plovdiv"]

commission_dict = {
    "Sofia": {
        "level_1": 5.00,    # 0 ≤ s ≤ 500
        "level_2": 7.00,    # 500 < s ≤ 1 000
        "level_3": 8.00,    # 1 000 < s ≤ 10 000
        "level_4": 12.00     # s > 10 000
    },
    "Varna": {
        "level_1": 4.50,  # 0 ≤ s ≤ 500
        "level_2": 7.50,  # 500 < s ≤ 1 000
        "level_3": 10.00,  # 1 000 < s ≤ 10 000
        "level_4": 13.00  # s > 10 000
    },
    "Plovdiv": {
        "level_1": 5.50,  # 0 ≤ s ≤ 500
        "level_2": 8.00,  # 500 < s ≤ 1 000
        "level_3": 12.00,  # 1 000 < s ≤ 10 000
        "level_4": 14.50  # s > 10 000
    }
}

if 0 <= sales <= 500:
    level = "level_1"
elif 500 < sales <= 1000:
    level = "level_2"
elif 100 < sales <= 10000:
    level = "level_3"
elif sales > 10000:
    level = "level_4"

if city in cities and sales >= 0:
    result = sales * (commission_dict[city][level] / 100)
    print(f"{result:.2f}")
else:
    print(f"error")
