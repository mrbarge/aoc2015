import re

with open('data/day8.input') as f:
    data = [e.strip() for e in f.readlines()]

chrcount = strcount = 0

for line in data:
    chrcount += len(line)
    line = re.sub('\\\\x..',' ',line.replace('\\\\',' ').replace('\\\"',' '))
    strcount += len(line)-2
    print(line)

print(f"Part one: {chrcount-strcount}")

p2strcount = 0
for line in data:
    p2strcount += len(line.replace('"','  ').replace('\"','    ').replace('\\','  ')) + 2
print(f"Part two: {p2strcount-chrcount}")
