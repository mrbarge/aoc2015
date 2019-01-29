with open('data/day23.input') as f:
    data = [e.strip() for e in f.readlines()]

registers = {
    'a': 1,
    'b': 0
}

ptr = 0
while ptr < len(data):

    elems = data[ptr].split()

    if elems[0] == 'jio':
        dest = elems[1][:-1]
        destval = int(elems[2])
        if registers[dest] == 1:
            ptr += destval
        else:
            ptr += 1
    elif elems[0] == 'inc':
        dest = elems[1]
        registers[dest] += 1
        ptr += 1
    elif elems[0] == 'tpl':
        dest = elems[1]
        registers[dest] *= 3
        ptr += 1
    elif elems[0] == 'jmp':
        val = int(elems[1])
        ptr += val
    elif elems[0] == 'jie':
        dest = elems[1][:-1]
        destval = int(elems[2])
        if registers[dest] % 2 == 0:
            ptr += destval
        else:
            ptr += 1
    elif elems[0] == 'hlf':
        dest = elems[1]
        registers[dest] /= 2
        ptr += 1
    else:
        print(f"Bad line: {line}")

print(registers["b"])
