hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

exam = (hour_exam * 60) + minute_exam
arrival = (hour_arrival * 60) + minute_arrival

diff_time = exam - arrival
if diff_time < 0:
    print(f"Late")
    if abs(diff_time) < 60:
        print(f"{abs(diff_time)} minutes after the start")
    else:
        h = abs(diff_time) // 60
        m = str(abs(diff_time) % 60).zfill(2)
        print(f"{h}:{m} hours after the start")

elif (diff_time >= 0) and (diff_time <= 30):
    print(f"On time")
    if diff_time != 0:
        print(f"{diff_time} minutes before the start")
else:
    print(f"Early")
    if diff_time < 60:
        print(f"{diff_time} minutes before the start")
    else:
        h = diff_time // 60
        m = str(diff_time % 60).zfill(2)
        print(f"{h}:{m} hours before the start")
