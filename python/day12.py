import json
import numbers


def count_nums(d, part2=False):
    if isinstance(d,dict):
        if part2 and 'red' in d.values():
            return 0
        return sum([count_nums(v,part2) for v in d.values()])
    elif any(isinstance(d,t) for t in (list, tuple)):
        return sum([count_nums(i,part2) for i in d])
    elif isinstance(d, numbers.Number):
        return d
    else:
        return 0


with open('data/day12.input') as f:
    data = json.load(f)

x = count_nums(data)
print(x)

y = count_nums(data,True)
print(y)