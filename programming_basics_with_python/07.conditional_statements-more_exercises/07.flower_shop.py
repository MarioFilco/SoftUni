from math import floor
from math import ceil

magnets = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

price_magnets = 3.25
price_hyacinths = 4.00
price_roses = 3.50
price_cacti = 8.00

order_sum = ((magnets * price_magnets) + (hyacinths * price_hyacinths) + (roses * price_roses) + (cacti * price_cacti)) * (1 - 0.05)

diff = gift_price - order_sum
if diff > 0:
    print(f"She will have to borrow {ceil(diff)} leva.")
else:
    print(f"She is left with {floor(abs(diff))} leva.")
