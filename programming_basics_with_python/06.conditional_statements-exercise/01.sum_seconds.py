time_1 = int(input())
time_2 = int(input())
time_3 = int(input())

time_sums = time_1 + time_2 + time_3
hours = time_sums // 60
seconds = time_sums % 60

print(f"{hours}:{str(seconds).zfill(2)}")

# if seconds < 10:
#     print(f"{hours}:0{seconds}")
# else:
#     print(f"{hours}:{seconds}")

