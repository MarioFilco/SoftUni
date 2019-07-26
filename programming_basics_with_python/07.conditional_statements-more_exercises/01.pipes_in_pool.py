v_liters = int(input())
p_1 = int(input())
p_2 = int(input())
h = float(input())

liters_p_1 = p_1 * h
liters_p_2 = p_2 * h
liters = liters_p_1 + liters_p_2
pool_full_percentage = (liters / v_liters) * 100
percentage_p_1 = (liters_p_1 / liters) * 100
percentage_p_2 = (liters_p_2 / liters) * 100
if liters_p_1 + liters_p_2 > v_liters:
    print(f"For {h:.2f} hours the pool overflows with {(liters - v_liters):.2f} liters.")
else:
    print(f"The pool is {pool_full_percentage:.2f}% full. Pipe 1: {percentage_p_1:.2f}%. Pipe 2: {percentage_p_2:.2f}%.")
