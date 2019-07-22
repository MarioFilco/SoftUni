speed = float(input())

if speed <= 10:
    print(f"slow")
elif (speed > 10) and (speed <= 50):
    print(f"average")
elif (speed > 50) and (speed <= 150):
    print(f"fast")
elif (speed > 150) and (speed <= 1000):
    print(f"ultra fast")
elif speed > 1000:
    print(f"extremely fast")
