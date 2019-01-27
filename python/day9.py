from collections import defaultdict
from itertools import permutations

with open('data/day9.input') as f:
    data = [e.strip() for e in f.readlines()]

routes = defaultdict(dict)

towns = set()
for line in data:
    from_town = line.split()[0]
    to_town = line.split()[2]
    distance = int(line.split()[4])
    routes[from_town][to_town] = distance
    routes[to_town][from_town] = distance
    towns.add(from_town)
    towns.add(to_town)

min_dist = 10**100
max_dist = 0
for route in permutations(towns):

    valid_route = True
    for x in range(0,len(route)-1):
        f = route[x]
        t = route[x+1]
        if f not in routes or t not in routes[f]:
            valid_route = False
            break

    if valid_route:
        d = sum([routes[route[x]][route[x+1]] for x in range(0,len(route)-1)])
        if d < min_dist:
            min_dist = d
        if d > max_dist:
            max_dist = d
print(f"Part one: {min_dist}")
print(f"Part two: {max_dist}")