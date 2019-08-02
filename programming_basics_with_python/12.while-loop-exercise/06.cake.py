width = int(input())
length = int(input())

cake_parts = width * length
parts = 0
part = input()
while part != "STOP":
    part = int(part)
    parts += part
    if cake_parts < parts:
        break
    part = input()
diff = cake_parts - parts
if diff < 0:
    print(f"No more cake left! You need {abs(diff)} pieces more.")
else:
    print(f"{cake_parts - parts} pieces are left.")

# width_pieces = int(input())
# length_pieces = int(input())
# pieces = input()
# count = 0
# while not pieces == 'STOP':
#     count += int(pieces)
#     if count > (width_pieces * length_pieces):
#         print(f"No more cake left! You need {count - (width_pieces * length_pieces)} pieces more.")
#         break
#     pieces = input()
# diff = count - (width_pieces * length_pieces)
# if diff < 0:
#     print(f"{abs(diff)} pieces are left.")
