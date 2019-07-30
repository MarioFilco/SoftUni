from math import floor
year = input()
num_holidays = int(input())
h = int(input())

weeks = 48
if year == "leap":
    more_volleyball = 0.15
else:
    more_volleyball = 0
plays_sofia = (weeks - h) * (3 / 4)
plays_holidays = num_holidays * (2 / 3)
plays_birth_city = h
count = (plays_sofia + plays_holidays + plays_birth_city) * (1 + more_volleyball)
print(floor(count))
