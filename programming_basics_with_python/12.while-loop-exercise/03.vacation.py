budget = float(input())
money_hand = float(input())

count_spend = 0
count_days = 0

while True:
    type_action = input()
    money = float(input())
    count_days += 1
    if type_action == "spend":
        count_spend += 1
        money_hand -= money
        if money_hand < 0:
            money_hand = 0
    else:
        count_spend = 0
        money_hand += money
    if count_spend == 5:
        print(f"You can't save the money.")
        print(f"{count_days}")
        break
    if budget <= money_hand:
        print(f"You saved the money for {count_days} days.")
        break


# money_excursion = float(input())
# money_on_hand = float(input())
# counter_day = 0
# counter_day_spend = 0
# last_choice = None
#
# while not money_on_hand >= money_excursion:
#     action_spend_save = input()
#     sum_spend_save = float(input())
#     counter_day += 1
#     last_choice = action_spend_save
#     if action_spend_save == 'spend' and last_choice == 'spend':
#         counter_day_spend += 1
#     else:
#         counter_day_spend = 0
#     if counter_day_spend == 5:
#         print("You can't save the money.")
#         print(counter_day)
#         break
#     if action_spend_save == 'spend':
#         money_on_hand -= sum_spend_save
#         if money_on_hand < 0:
#             money_on_hand = 0
#     else:
#         money_on_hand += sum_spend_save
#
# if money_on_hand >= money_excursion:
#     print(f"You saved the money for {counter_day} days.")
