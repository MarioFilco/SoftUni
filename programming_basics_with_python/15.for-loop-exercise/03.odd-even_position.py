import sys

n = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize - 1
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize - 1

for n in range(1, n + 1):
    num = float(input())
    if n % 2 == 1:
        odd_sum += num
        if odd_min > num:
            odd_min = num
        if odd_max < num:
            odd_max = num
    else:
        even_sum += num
        if even_min > num:
            even_min = num
        if even_max < num:
            even_max = num

if n == 0:
    print(f"OddSum={odd_sum:.2f},")
    print("OddMin=No,")
    print("OddMax=No,")
    print(f"EvenSum={even_sum:.2f},")
    print("EvenMin=No,")
    print("EvenMax=No")
elif n == 1:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print("EvenMin=No,")
    print("EvenMax=No")

else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")

# n = int(input())
#
# num_list = []
# for _ in range(n):
#     num = float(input())
#     num_list.append(num)
# odd_num_list = [x for x in num_list if num_list.index(x) % 2 == 0]
# even_num_list = [x for x in num_list if num_list.index(x) % 2 != 0]
#
# odd_sum = sum(odd_num_list)
# if len(odd_num_list) > 0:
#     odd_min = min(odd_num_list)
#     odd_max = max(odd_num_list)
# else:
#     odd_min = "No"
#     odd_max = "No"
# even_sum = sum(even_num_list)
# if len(even_num_list) > 0:
#     even_min = min(even_num_list)
#     even_max = max(even_num_list)
# else:
#     even_min = "No"
#     even_max = "No"
# if odd_max == odd_min:
#     odd_max = "No"
#     odd_min = "No"
# if even_max == even_min:
#     even_max = "No"
#     even_min = "No"
# print(f"OddSum= {odd_sum:.2f}")
# print(f"OddMin= {odd_min}")
# print(f"OddMax= {odd_max}")
# print(f"EvenSum= {even_sum:.2f}")
# print(f"EvenMin= {even_min}")
# print(f"EvenMax= {even_max}")
