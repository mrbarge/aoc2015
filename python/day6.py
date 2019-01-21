import re

with open('data/day6.input') as f:
    data = [e.strip() for e in f.readlines()]


def process(data, part2=False):
    grid = [[0 for x in range(0, 1000)] for y in range(0, 1000)]
    for line in data:
        matches = re.findall(r'.* (\d+),(\d+) through (\d+),(\d+)', line)
        if matches:
            x1 = int(matches[0][0])
            y1 = int(matches[0][1])
            x2 = int(matches[0][2])
            y2 = int(matches[0][3])
        else:
            print(f"Bad line: {line}")
        for yi in range(y1, y2 + 1):
            for xi in range(x1, x2 + 1):
                if line.startswith('turn on'):
                    if not part2:
                        grid[yi][xi] = 1
                    else:
                        grid[yi][xi] += 1
                elif line.startswith('turn off'):
                    if not part2:
                        grid[yi][xi] = 0
                    else:
                        grid[yi][xi] -= 1
                        if grid[yi][xi] < 0:
                            grid[yi][xi] = 0
                else:
                    if not part2:
                        grid[yi][xi] = not grid[yi][xi]
                    else:
                        grid[yi][xi] += 2

    if not part2:
        p1 = sum(x.count(1) for x in grid)
        print(f"Part one: {p1}")
    else:
        p2 = sum(sum(x) for x in grid)
        print(f"Part two: {p2}")


process(data)
process(data, True)
