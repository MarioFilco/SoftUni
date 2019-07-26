from sys import maxsize

number_kilometers = int(input())
day_night = input()

taxi_sum = maxsize
bus_sum = maxsize
train_sum = maxsize

if number_kilometers >= 100:
    train_sum = number_kilometers * 0.06
if number_kilometers >= 20:
    bus_sum = number_kilometers * 0.09
if day_night == "day":
    taxi_sum = number_kilometers * 0.79 + 0.70
elif day_night == "night":
    taxi_sum = number_kilometers * 0.90 + 0.70

result = min([taxi_sum, bus_sum, train_sum])
print(f"{result:.2f}")
