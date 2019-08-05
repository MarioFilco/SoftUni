num = int(input())

for n in range(1, num + 1):
    is_flour = False
    is_eggs = False
    is_sugar = False
    while True:
        product = input()
        if product == 'flour':
            is_flour = True
        if product == 'eggs':
            is_eggs = True
        if product == 'sugar':
            is_sugar = True
        if product == 'Bake!':
            if is_flour and is_eggs and is_sugar:
                print(f'Baking batch number {n}...')
                break
            else:
                print('The batter should contain flour, eggs and sugar!')
