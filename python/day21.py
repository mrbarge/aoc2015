from itertools import combinations

class Fighter:

    def __init__(self, hp=100, damage=0, armor=0):
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.build_cost = 0
        self.items = []

    def apply(self, item):
        self.damage += item.damage
        self.armor += item.armor
        self.build_cost += item.cost
        self.items.append(item.name)

    def show(self):
        print(f"HP: {self.hp} Damage: {self.damage} Armor: {self.armor}")

class Item:

    def __init__(self, name, cost=0, damage=0, armor=0):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor


weapons = [
    Item('dagger', 8, 4, 0),
    Item('shortsword', 10, 5, 0),
    Item('warhammer', 25, 6, 0),
    Item('longsword', 40, 7, 0),
    Item('greataxe', 74, 8, 0)
]

armors = [
    Item('leather', 13, 0, 1),
    Item('chainmail', 31, 0, 2),
    Item('splitmail', 53, 0, 3),
    Item('bandedmail', 75, 0, 4),
    Item('platemail', 102, 0, 5),
    Item('none', 0, 0, 0),
]

rings = [
    Item('da1', 25, 1, 0),
    Item('da2', 50, 2, 0),
    Item('da3', 100, 3, 0),
    Item('de1', 20, 0, 1),
    Item('de2', 40, 0, 2),
    Item('de3', 80, 0, 3),
    Item('none1', 0, 0, 0),
    Item('none2', 0, 0, 0),
]


def fight(player, boss):
    while True:
        player.hp -= (boss.damage - player.armor)
        # don't do boss attack if already dead
        if boss.hp > 0:
            boss.hp -= (player.damage - boss.armor)

        if boss.hp <= 0:
            return True
        elif player.hp <= 0:
            return False


player = Fighter(hp=100, damage=0, armor=0)
boss = Fighter(hp=100, damage=8, armor=2)

successful_costs = []
unsuccessful_costs = []

# get all possible combinations of ring wearings
ring_combos = list(combinations(rings,2))

# iterate over every weapon
for weapon in weapons:
    # iterate over every armor
    for armor in armors:
        # iterate over each ring combo
        for ring_combo in ring_combos:
            # set up the players
            boss = Fighter(hp=100, damage=8, armor=2)
            player = Fighter(hp=100, damage=0, armor=0)
            # gear up the player
            player.apply(weapon)
            player.apply(armor)
            player.apply(ring_combo[0])
            player.apply(ring_combo[1])

            # time to FIGHT!!
            running_cost = weapon.cost + armor.cost + ring_combo[0].cost + ring_combo[1].cost
            if fight(player,boss):
                # how much did it cost?
                successful_costs.append(running_cost)
            else:
                unsuccessful_costs.append(running_cost)

successful_costs = sorted(successful_costs)
unsuccessful_costs = sorted(unsuccessful_costs,reverse=True)
print(f"Part one: {successful_costs[0]}")
print(unsuccessful_costs)
print(f"Part two: {unsuccessful_costs[0]}")