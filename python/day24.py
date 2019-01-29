from functools import reduce
from itertools import combinations
from operator import mul

with open('data/day24.input') as f:
    data = [int(e.strip()) for e in f.readlines()]

total_weight = sum(data)

qe = 10**100
group_weight = total_weight // 3
# print(f"Looking for {group_weight}")
for group_length in range(4,(len(data) // 3)):
    for c in combinations(data, group_length):
        combo = list(c)
        if sum(list(combo)) == group_weight:
            qe = min(reduce(mul, combo, 1),qe)
print(f"Part one: {qe}")

qe = 10**100
group_weight = total_weight // 4
for group_length in range(4,(len(data) // 3)):
    for c in combinations(data, group_length):
        combo = list(c)
        if sum(list(combo)) == group_weight:
            qe = min(reduce(mul, combo, 1),qe)
print(f"Part two: {qe}")
