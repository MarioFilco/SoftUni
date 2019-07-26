age = float(input())
sex = input()

if sex == "m":
    if age >= 16:
        title = "Mr."
    else:
        title = "Master"
else:
    if age >= 16:
        title = "Ms."
    else:
        title = "Miss"

print(title)
