def wrapping_area(l, w, h):
    sides = sorted([(l*w), (w*h), (h*l)])
    area = sum(list(map(lambda x: x*2, sides))) + sides[0]
    return area

def ribbon(l, w, h):
    sides = sorted([((l * w),l,w), ((w * h),w,h), ((h * l),h,l)], key=lambda t: t[0])
    ribbon = 2*sides[0][1] + 2*sides[0][2] + (l*w*h)
    return ribbon

with open('data/day2.input') as f:
    data = [e.strip().split('x') for e in f.readlines()]

total_area = 0
for present in data:
    total_area += wrapping_area(int(present[0]),int(present[1]),int(present[2]))
print(f"Part 1: {total_area}")

total_ribbon = 0
for present in data:
    total_ribbon += ribbon(int(present[0]),int(present[1]),int(present[2]))
print(f"Part 2: {total_ribbon}")

