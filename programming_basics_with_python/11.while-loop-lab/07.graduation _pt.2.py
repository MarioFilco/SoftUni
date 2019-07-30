name = input()
grades = 1
sum_ = 0

while grades <= 12:
    grade = float(input())
    if grade >= 4:
        grades += 1
        sum_ += grade
    else:
        break
average = sum_ / 12
if grade < 4:
    print(f"{name} has been excluded at {grades} grade")
else:
    print(f"{name} graduated. Average grade: {average:.2f}")


# name = input()
# counter_class = 0
# grades = 0
# count_bad_grade = 0
#
# while True:
#     grade = float(input())
#     grades += grade
#     if grade < 4:
#         count_bad_grade += 1
#         if count_bad_grade == 2:
#             print(f"{name} has been excluded at {counter_class} grade")
#             break
#     counter_class += 1
#     if counter_class >= 12:
#         average = grades / counter_class
#         print(f"{name} graduated. Average grade: {average:.2f}")
#         break
