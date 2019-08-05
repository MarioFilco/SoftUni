num_open_site = int(input())
salary = int(input())

for _ in range(num_open_site):
    name_site = input()
    if name_site == 'Facebook':
        fine = 150
    elif name_site == 'Instagram':
        fine = 100
    elif name_site == 'Reddit':
        fine = 50
    else:
        fine = 0
    salary -= fine
    if salary <= 0:
        break

if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
