length = float(input())
width = float(input())

columns = (width - (100 / 100)) // (70 / 100)
rows = length // (120 / 100)
seats = (columns * rows) - 1 - 2
print(f"{seats:g}")
