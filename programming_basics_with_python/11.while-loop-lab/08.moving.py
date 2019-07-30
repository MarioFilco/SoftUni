length = int(input())
width = int(input())
height = int(input())

cubic = length * width * height
total_cartons = 0
br = False
while total_cartons < cubic:
    cartons = input()
    if cartons == "Done":
        break
    cartons = int(cartons)
    total_cartons += cartons
    if total_cartons > cubic:
        br = True
        break
if br:
    print(f"No more free space! You need {total_cartons - cubic} Cubic meters more.")
else:
    print(f"{abs(total_cartons - cubic)} Cubic meters left.")

# width = int(input())
# length = int(input())
# height = int(input())
#
# cubic = width * length * height
# cartons = input()
# cartons_cobic = 0
#
# while not cartons == 'Done':
#     cartons_cobic += int(cartons)
#     if cartons_cobic >= cubic:
#         break
#     cartons = input()
#
# diff = cubic - cartons_cobic
#
# if diff < 0:
#     print(f"No more free space! You need {abs(diff)} Cubic meters more.")
# else:
#     print(f"{diff} Cubic meters left.")
