price_mackerel = float(input())
price_sprats = float(input())
bonito = float(input())
mackerel = float(input())
mussels = int(input())

price_bonito = price_mackerel * (1 + 0.60)
price_mackerel = price_sprats * (1 + 0.80)
price_mussels = 7.50
money = (bonito * price_bonito) + (mackerel * price_mackerel) + (mussels * price_mussels)
money = round(money, 2)
print(f"{money:.2f}")
