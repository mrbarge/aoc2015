with open('data/day1.input') as f:
    data = f.readline().strip()

level = i = basement = 0

while i < len(data):
    if data[i] == '(':
        level += 1
    elif data[i] == ')':
        level -= 1

    if level < 0 and basement < 1:
        basement = i+1

    i += 1

print(f"Part one: {level}")
print(f"Part two: {basement}")
