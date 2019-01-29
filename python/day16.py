import re


class Sue:
    def __init__(self, id, attributes):
        self.id = id
        self.attributes = attributes


def count_common(s,t):
    return sum([True for att in t.keys() if att in s.attributes and s.attributes[att] == t[att]])

def count_p2_common(s,t):
    common = 0
    for att in t.keys():
        if att in s.attributes:
            if att in ['cats','trees'] and s.attributes[att] > t[att]:
                common += 1
            elif att in ['pomeranians','goldfish'] and s.attributes[att] < t[att]:
                common += 1
            elif att not in ['pomeranians','goldfish','cats','trees'] and s.attributes and s.attributes[att] == t[att]:
                common += 1
    return common

with open('data/day16.input') as f:
    data = [e.strip() for e in f.readlines()]

sues = []
target = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for line in data:
    elems = line.split()
    atts = {}
    id = int(elems[1][:-1])
    atts[elems[2][:-1]] = int(elems[3][:-1])
    atts[elems[4][:-1]] = int(elems[5][:-1])
    atts[elems[6][:-1]] = int(elems[7])
    sues.append(Sue(id,atts))

max_match = 0
sue_match = 0

for sue in sues:
    matching = count_common(sue, target)
    if matching > max_match:
        max_match = matching
        sue_match = sue.id
print(f"PArt one: {sue_match}")

max_match = 0
sue_match = 0
for sue in sues:
    matching = count_p2_common(sue, target)
    if matching > max_match:
        max_match = matching
        sue_match = sue.id
print(f"Part two: {sue_match}")

