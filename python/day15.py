import itertools

class Ingredient:

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories


def total_score(d):
    capacity = durability = flavor = texture = 0
    for ingredient, quantity in dict(d).items():
        capacity += ingredient.capacity * quantity
        durability += ingredient.durability * quantity
        flavor += ingredient.flavor * quantity
        texture += ingredient.texture * quantity
        # print(f"Doing {ingredient.name} with {quantity} and {capacity} {durability} {flavor} {texture}")
    return max(0,capacity) * max(0,durability) * max(0,flavor) * max(0,texture)


def total_cals(d):
    calories = 0
    for ingredient, quantity in dict(d).items():
        calories += ingredient.calories * quantity
    return max(0,calories)


ingredients = [
    Ingredient('sugar',     capacity=3,     durability=0,   flavor=0,   texture=-3, calories=2),
    Ingredient('sprinkles', capacity=-3,    durability=3,   flavor=0,   texture=0,  calories=9),
    Ingredient('candy',     capacity=-1,    durability=0,   flavor=4,   texture=0,  calories=1),
    Ingredient('chocolate', capacity=0,     durability=0,   flavor=-2,  texture=2,  calories=8)
]

nums = list(range(0,101))
# combinations = [seq for seq in itertools.combinations(nums, 4) if sum(seq) == 100]
combinations = []
for a in range(101):
  for b in range(101):
    for c in range(101):
      d = 100-a-b-c
      if d < 0: break
      else: combinations.append([a,b,c,d])

max_score = 0
for combo in combinations:
    ingredient_combo = {ingredients[x]: combo[x] for x in range(0,len(combo))}
    score = total_score(ingredient_combo)
    calories = total_cals(ingredient_combo)
    if calories == 500:
        max_score = max(max_score, total_score(ingredient_combo))

print(max_score)
