import re
s = '1-5,7,9,10-13'

r = [
  eval('['+re.sub('(\d+)-(\d+)', r'*range(\1, \2+1)', s)+']')
]
print(r)