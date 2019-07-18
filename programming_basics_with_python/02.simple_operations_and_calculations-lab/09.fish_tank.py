length = int(input())
width = int(input())
height = int(input())
percent = float(input())

litres = length * width * height * 0.001
litres_net = litres * (1 - (percent / 100))
print(f"{litres_net:.3f}")
