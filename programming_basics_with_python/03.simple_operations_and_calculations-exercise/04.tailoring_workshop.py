num_tables = int(input())
length = float(input())
width = float(input())

usd = 1.85
cover_table_big = (width + 0.60) * (length + 0.60)
cover_table_small = length / 2 * length / 2
price_usd = (cover_table_big * num_tables * 7) + (cover_table_small * num_tables * 9)
print(f"{price_usd:.2f} USD")
print(f"{price_usd * usd:.2f} BGN")
