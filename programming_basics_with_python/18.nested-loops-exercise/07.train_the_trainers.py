judge = int(input())
average_rating = 0
counter_presentations = 0
while True:
    sum_rating = 0
    presentations = input()
    if presentations == 'Finish':
        average_final_rating = average_rating / counter_presentations
        print(f'Student\'s final assessment is {average_final_rating:.2f}.')
        break
    for n in range(1, judge + 1):
        rating = float(input())
        sum_rating += rating
    counter_presentations += 1
    average = sum_rating / judge
    average_rating += average
    print(f'{presentations} - {average:.2f}.')
