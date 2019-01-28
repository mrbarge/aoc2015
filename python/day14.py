import operator

class Reindeer:

    def __init__(self, distance, duration, rest):
        self.velocity = distance
        self.max_duration = duration
        self.max_rest = rest
        self.distance_travelled = 0
        self.rest_period = 0
        self.fly_period = 0
        self.points = 0

    def fly(self):
        if self.rest_period > 0:
            # need to rest some more
            self.rest_period -= 1
        else:
            self.distance_travelled += self.velocity
            self.fly_period += 1

            # check if we need to rest
            if self.fly_period == self.max_duration:
                self.rest_period = self.max_rest
                self.fly_period = 0


def travel(r, time=0):
    for t in range(0,time):
        r.fly()
    return r.distance_travelled


with open('data/day14.input') as f:
    data = [e.strip() for e in f.readlines()]

reindeers = []

for line in data:
    distance = int(line.split()[3])
    duration = int(line.split()[6])
    rest = int(line.split()[13])

    reindeers.append(Reindeer(distance, duration, rest))

max = 0
for t in range(0,2503):
    for r in reindeers:
        r.fly()
    reindeers.sort(key=operator.attrgetter('distance_travelled'))
    max_distance = reindeers[-1].distance_travelled
    # award points to all reindeers flying that distance
    for r in reindeers:
        if r.distance_travelled == max_distance:
            r.points += 1

print(f"Part one: {reindeers[-1].distance_travelled}")

reindeers.sort(key=operator.attrgetter('points'))
print(f"Part two: {reindeers[-1].points}")