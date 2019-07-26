screening_type = input()
rows = int(input())
columns = int(input())

price_ticket = {
    "Premiere": 12.00,
    "Normal": 7.50,
    "Discount": 5.00
}
income = price_ticket[screening_type] * rows * columns
print(f"{income:.2f} leva")
