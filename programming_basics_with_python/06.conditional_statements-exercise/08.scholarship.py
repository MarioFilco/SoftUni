income = float(input())
average_success = float(input())
min_wage = float(input())

scholarship_for_excellent_success = average_success * 25
social_scholarship = min_wage * 0.35
if ((income < min_wage) and average_success > 4.50) and average_success >= 5.50:
    if scholarship_for_excellent_success >= social_scholarship:
        print(f"You get a scholarship for excellent results {int(scholarship_for_excellent_success)} BGN")
    else:
        print(f"You get a Social scholarship {int(social_scholarship)} BGN")
elif average_success >= 5.50:
    print(f"You get a scholarship for excellent results {int(scholarship_for_excellent_success)} BGN")
elif (income < min_wage) and average_success > 4.50:
    print(f"You get a Social scholarship {int(social_scholarship)} BGN")
else:
    print(f"You cannot get a scholarship!")
