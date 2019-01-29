import copy
import sys

def neighbours(x,y,maxX,maxY):
    possible = [(x-1,y),(x+1,y),(x,y-1),(x,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]
    ret = [p for p in possible if valid(p,maxX,maxY)]
    return ret

def valid(coord,maxX,maxY):
    return (coord[0] >= 0 and coord[0] <= maxX and coord[1] >= 0 and coord[1] <= maxY)


def count_on(coords,data):
    return sum([1 for coord in coords if data[coord[1]][coord[0]]])


def tick(grid):
    newgrid = copy.deepcopy(grid)

    for y in range(0,len(grid)):
        for x in range(0,len(grid[0])):
            n = neighbours(x,y,len(grid)-1,len(grid)-1)
            if grid[y][x]:
                if 2 <= count_on(n,grid) <= 3:
                    newgrid[y][x] = True
                else:
                    newgrid[y][x] = False
            elif not grid[y][x] and (count_on(n,grid) == 3):
                newgrid[y][x] = True
            else:
                newgrid[y][x] = False
    newgrid[0][0] = newgrid[99][0] = newgrid[0][99] = newgrid[99][99] = True
    return newgrid


def print_grid(grid):
    for y in range(0,100):
        for x in range(0,100):
            if grid[y][x]:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')

grid = [[False for x in range(0,100)] for y in range(0,100)]
grid[0][0] = grid[99][0] = grid[0][99] = grid[99][99] = True

with open('data/day18.input') as f:
    data = [e.strip() for e in f.readlines()]

y = 0
for line in data:
    for x in range(0,len(line)):
        if line[x] == '#':
            grid[y][x] = True
        else:
            grid[y][x] = False
    y += 1

for x in range(0,100):
    grid = tick(grid)

on = sum([sum([c for c in line if c]) for line in grid])
print(on)

