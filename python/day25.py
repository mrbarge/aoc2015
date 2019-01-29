class Pos:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        self.maxY=y

    def move_to_next_pos(self):
        if (self.y-1) < 0:
            # need to start a new diag sweep
            self.y = self.maxY + 1
            self.maxY += 1
            self.x = 0
        else:
            self.x += 1
            self.y -= 1

input_row = 2947
input_col = 3029

grid = [[float(0) for x in range(0,7000)] for y in range(0,7000)]

p = Pos(0,1)
prev = 20151125
while p.y < 7000:
    val = (prev * 252533) % 33554393
    grid[p.y][p.x] = val
    p.move_to_next_pos()
    prev = val

print(f"Part one: {grid[input_row-1][input_col-1]}")
