num = float(input())
in_ = input()
out_ = input()

units_dict = {
    "m": 1,
    "cm": 100,
    "mm": 1000
}
result = num * units_dict[out_] / units_dict[in_]

print(f"{result:.3f}")
