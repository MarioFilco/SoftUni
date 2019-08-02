n = int(input())

num_list = []
for _ in range(n):
    number = int(input())
    num_list.append(number)

print(f"Max number: {max(num_list)}")
print(f"Min number: {min(num_list)}")
