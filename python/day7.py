import re


def check_lvals(s, w):
    for token in s.split():
        if token.isdigit():
            continue
        elif token in ['NOT', 'LSHIFT', 'RSHIFT', 'AND', 'OR']:
            continue
        elif token not in w.keys():
            return False
    return True


def get_next_inst(data, wires, seen):
    # find all the assignments first
    for line in data:

        if line in seen.keys():
            continue

        m = re.findall(r'^(.+) -> (.+)$', line)
        if m and check_lvals(m[0][0], wires):
            return line

    return None


def extract_args(s, wires):
    l1 = s.split()[0]
    l2 = s.split()[2]
    if l1.isdigit():
        l1 = int(l1)
    else:
        l1 = wires[l1]
    if l2.isdigit():
        l2 = int(l2)
    else:
        l2 = wires[l2]
    return l1, l2

def process(line, w):
    m = re.findall(r'^(\d+) -> (.+)$', line)
    m2 = re.findall(r'^(\w+) -> (.+)$', line)
    if m:
        lval = int(m[0][0])
        rval = m[0][1]
        w[rval] = lval
    elif m2:
        lval = wires[m2[0][0]]
        rval = m2[0][1]
        w[rval] = lval
    elif line.startswith('NOT '):
        lval = line.split()[1]
        rval = line.split()[3]
        w[rval] = ~ w[lval]
    elif line.split()[1] in ['AND','OR','LSHIFT','RSHIFT']:
        lval1, lval2 = extract_args(line.split('->')[0], wires)
        rval = line.split()[4]
        if 'AND' in line:
            w[rval] = lval1 & lval2
        elif 'OR' in line:
            w[rval] = lval1 | lval2
        elif 'LSHIFT' in line:
            w[rval] = lval1 << lval2
        elif 'RSHIFT' in line:
            w[rval] = lval1 >> lval2
        else:
            print(f"Unknown command: {line}")

    return w

with open('data/day7.input') as f:
    data = [e.strip() for e in f.readlines()]

wires = {}
seen = {}
line = get_next_inst(data, wires, seen)
while line:
    wires = process(line, wires)
    seen[line] = True
    line = get_next_inst(data, wires, seen)
print(f"Part one: {wires['a']}")

with open('data/day7-2.input') as f:
    data = [e.strip() for e in f.readlines()]
wires = {}
seen = {}
line = get_next_inst(data, wires, seen)
while line:
    wires = process(line, wires)
    seen[line] = True
    line = get_next_inst(data, wires, seen)
print(f"Part two: {wires['a']}")
