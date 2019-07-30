payments = int(input())
total = 0

while payments:
    deposit = float(input())
    if deposit < 0:
        print(f"Invalid operation!")
        break
    print(f"Increase: {deposit:.2f}")
    total = total + deposit
    payments -= 1
print(f"Total: {total:.2f}")
