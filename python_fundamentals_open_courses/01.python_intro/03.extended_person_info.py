def print_data(name, age, town, salary, age_range, salary_range):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Town: {town}")
    print(f"Salary: ${salary:.2f}")
    print(f"Age range: {age_range}")
    print(f"Salary range: {salary_range}")


def _range(age, salary):
    if age < 18:
        age_r = 'teen'
    elif age < 70:
        age_r = 'adult'
    else:
        age_r = 'elder'

    if salary < 500:
        salary_r = 'low'
    elif salary < 2000:
        salary_r = 'medium'
    else:
        salary_r = 'high'
    return age_r, salary_r


def input_data():
    name = input()
    age = int(input())
    town = input()
    salary = float(input())
    age_range, salary_range = _range(age, salary)
    print_data(name, age, town, salary, age_range, salary_range)


input_data()