name_winner = None
max_sum_letter = -1
current_sum = 0

while True:
    name = input()
    if name == 'STOP':
        break
    for letter in name:
        current_number = ord(letter)
        current_sum += current_number
        if current_sum > max_sum_letter:
            max_sum_letter = current_sum
            name_winner = name
    current_sum = 0

print(f'Winner is {name_winner} - {max_sum_letter}!')
