from math import floor

length = float(input())
width = float(input())
wardrobe_side = float(input())

area = (length * 100) * (width * 100)
wardrobe = (wardrobe_side * 100) * (wardrobe_side * 100)
bench = area / 10
hall = area - wardrobe - bench
dancer_area = 40 + 7000
dancers = floor(hall / dancer_area)
print(dancers)
