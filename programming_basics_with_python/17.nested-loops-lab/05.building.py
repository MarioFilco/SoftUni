numbers_floors = int(input())
numbers_rooms = int(input())

for floor in range(numbers_floors, 0, -1):
    for room in range(numbers_rooms):
        if numbers_floors == floor:
            print(f'L{floor}{room}', end=' ')
        else:
            if floor % 2 == 1:
                print(f'A{floor}{room}', end=' ')
            else:
                print(f'O{floor}{room}', end=' ')
    print()
