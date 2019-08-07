num = int(input())
count = 1
is_stop = None
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(f'{count} ', end='')
        if count >= num:
            is_stop = True
            break
        count += 1
    if is_stop:
        break
    print()
