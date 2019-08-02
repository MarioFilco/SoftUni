n = int(input())

sum_left = 0
sum_right = 0
left = True
for i in range(n):
    sum_left += int(input())
for i in range(n):
    sum_right += int(input())
if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {abs(sum_left - sum_right)}")
