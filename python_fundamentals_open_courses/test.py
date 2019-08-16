import re
s = '1-5,7,9,10-13'

r = [
  eval('['+re.sub('(\d+)-(\d+)', r'*range(\1, \2+1)', s)+']')
]
print(r)


print((lambda t: t == t[::-1])(input().lower()))

print("".join(map(lambda x: "Happy birthday to " + ("you " if x != 2 else f"dear {input()} "), range(4))))