while True:
    saved_money = 0
    country = input()
    if country == 'End':
        break
    budget = float(input())
    while not saved_money >= budget:
        money = float(input())
        saved_money += money
        if saved_money >= budget:
            print(f'Going to {country}!')
            break
