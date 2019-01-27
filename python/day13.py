from collections import defaultdict
from itertools import permutations
from copy import deepcopy

def score(names, rules):
    ret = 0
    num_names = len(names)
    for i in range(0, num_names):
        pi = i-1
        if pi < 0:
            pi = len(names)-1
        ni = (i+1) % num_names
        name_from = names[i]
        name_next = names[ni]
        name_prev = names[pi]

        if name_next in (rules[name_from]).keys():
            ret += rules[name_from][name_next]
        else:
            return None

        if name_prev in (rules[name_from]).keys():
            ret += rules[name_from][name_prev]
        else:
            return None
    return ret


def part_two_data(names, rules):
    newrules = deepcopy(rules)
    for name in names:
        newrules[name]["dummy"] = 0
        newrules["dummy"][name] = 0
    return newrules


with open('data/day13.input') as f:
    data = [e.strip() for e in f.readlines()]

rules = defaultdict(lambda: defaultdict(int))

for line in data:
    elems = line.split()
    name_from = elems[0]
    name_to = elems[10][:-1]
    units = int(elems[3])

    if elems[2] == 'lose':
        units *= -1

    rules[name_from][name_to] = units

names = list(rules.keys())
max_score = 0
for perm in permutations(names):
    s = score(perm,rules)
    if s > max_score:
        max_score = s

print(f"Part one: {max_score}")

rules = part_two_data(names, rules)
names += ["dummy"]
max_score = 0
for perm in permutations(names):
    s = score(perm,rules)
    if s > max_score:
        max_score = s

print(f"Part two: {max_score}")
