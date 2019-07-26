hours_need = int(input())
days = int(input())
number = int(input())

days_work = days * (1 - 0.10)
hours_works = (days_work * 8) + (number * 2 * days)
diff = int(hours_works) - hours_need
if diff >= 0:
    print(f"Yes!{int(diff)} hours left.")
else:
    print(f"Not enough time!{int(abs(diff))} hours needed.")
