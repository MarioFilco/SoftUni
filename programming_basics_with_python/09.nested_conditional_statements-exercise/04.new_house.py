type_flower = input()
quality_flower = int(input())
budget = int(input())

discount = 0
more_expensive = 0
flowers_dict = {
    "Roses": 5.00,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3.00,
    "Gladiolus": 2.50
}


if type_flower == "Roses" and quality_flower > 80:
    discount = 0.10
elif type_flower == "Dahlias" and quality_flower > 90:
    discount = 0.15
elif type_flower == "Tulips" and quality_flower > 80:
    discount = 0.15
elif type_flower == "Narcissus" and quality_flower < 120:
    more_expensive = 0.15
elif type_flower == "Gladiolus" and quality_flower < 80:
    more_expensive = 0.20

cost = flowers_dict[type_flower] * quality_flower * (1 - discount) * (1 + more_expensive)
diff = budget - cost
if diff >= 0:
    print(f"Hey, you have a great garden with {quality_flower} {type_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(diff):.2f} leva more.")
