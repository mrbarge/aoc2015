from functools import reduce
import operator

def deliver(elf,houses,part2=False):
    i = elf
    if not part2:
        while i < len(houses):
            houses[i] += (elf * 10)
            i += elf
    else:
        while i < (elf * 50) and i < len(houses):
            houses[i] += (elf * 11)
            i += elf
    return houses

def simulate(num_houses, input, part2=False):
    houses = [0 for x in range(0,num_houses)]
    for elf in range(1,num_houses):
        houses = deliver(elf,houses,part2)
    for i in range(1,num_houses):
        if houses[i] >= input:
            print(i)
            return True

input = 33100000
x = 800000
print(simulate(x,input,part2=False))
print(simulate(x,input,part2=True))
# while not simulate(x,input):
#     x += 1000
#     print(f"doing {x}")
#
