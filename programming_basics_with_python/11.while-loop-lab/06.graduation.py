name = input()
grades = 1
sum_ = 0

while grades <= 12:
    grade = float(input())
    if grade >= 4:
        grades += 1
        sum_ += grade
average = sum_ / 12
print(f"{name} graduated. Average grade: {average:.2f}")
