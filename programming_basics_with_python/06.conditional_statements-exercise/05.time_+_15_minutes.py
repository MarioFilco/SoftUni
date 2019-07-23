hours = int(input())
minutes = int(input())
minutes_plus_15_min = (hours * 60) + minutes + 15
hours = minutes_plus_15_min // 60
minutes = minutes_plus_15_min % 60
if hours > 23:
    hours = 0
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
