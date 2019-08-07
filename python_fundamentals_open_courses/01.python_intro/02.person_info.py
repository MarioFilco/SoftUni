def print_data(name, age, town, salary):
    print(f"{name} is {age} years old, is from {town} and makes ${salary}")


name = input()
age = int(input())
town = input()
salary = float(input())

print_data(name, age, town, salary)
