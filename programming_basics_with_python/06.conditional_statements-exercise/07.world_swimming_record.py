from math import floor
record = float(input())
meters = float(input())
seconds_per_meter = float(input())

time = meters * seconds_per_meter
resistance_seconds = floor(meters / 15) * 12.5
# resistance_seconds = int(meters / 15 * 12.5)
diff = record - (time + resistance_seconds)

if diff > 0:
    print(f"Yes, he succeeded! The new world record is {time + resistance_seconds:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(diff):.2f} seconds slower.")
