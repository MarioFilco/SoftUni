poor_grades_threshold = int(input())

count_exercises = 0
last_name_exercise = None
grades = 0
count_bed_grades = 0
exercise = input()
while exercise != "Enough":
    grade = int(input())
    if grade <= 4:
        count_bed_grades += 1
    count_exercises += 1
    if poor_grades_threshold == count_bed_grades:
        print(f"You need a break, {count_bed_grades} poor grades.")
        break

    grades += grade
    last_name_exercise = exercise
    exercise = input()

if exercise == "Enough":
    average_grades = grades / count_exercises
    print(f"Average score: {average_grades:.2f}")
    print(f"Number of problems: {count_exercises}")
    print(f"Last problem: {last_name_exercise}")


# count_bad_scores = int(input())
# bad_scores = 0
# sum_score_problem = 0
# counter_problem = 0
# problem = None
# while count_bad_scores:
#     problem = input()
#     if problem == 'Enough':
#         print(f"Average score: {average:.2f}")
#         print(f"Number of problems: {counter_problem}")
#         print(f"Last problem: {last_problem}")
#         break
#     score_problem = int(input())
#     if score_problem <= 4:
#         bad_scores += 1
#     if bad_scores == count_bad_scores:
#         print(f"You need a break, {bad_scores} poor grades.")
#         break
#     sum_score_problem += score_problem
#     counter_problem += 1
#     average = sum_score_problem / counter_problem
#     last_problem = problem