from collections import defaultdict

def move(dir, coord):
    if dir == '^':
        return coord[0], coord[1]-1
    elif dir == '>':
        return coord[0]+1, coord[1]
    elif dir == '<':
        return coord[0]-1, coord[1]
    else:
        return coord[0], coord[1]+1

with open('data/day3.input') as f:
    data = f.readline().strip()

seen = defaultdict(int)
coord = (0,0)
seen[coord] += 1
for dir in data:
    coord = move(dir, coord)
    seen[coord] += 1

print(f"Part one: {len(seen)}")

seen = defaultdict(int)
santacoord = (0,0)
robocoord = (0,0)
santaTurn = True

seen[santacoord] += 2
for dir in data:
    if santaTurn:
        santacoord = move(dir, santacoord)
        seen[santacoord] += 1
        santaTurn = False
    else:
        robocoord = move(dir, robocoord)
        seen[robocoord] += 1
        santaTurn = True

print(f"Part two: {len(seen)}")
