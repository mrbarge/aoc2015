from itertools import combinations

numbers = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]
result = [seq for i in range(len(numbers), 0, -1) for seq in combinations(numbers, i) if sum(seq) == 150]

print(len(result))
p2 = sum([1 for x in result if len(x) == 4])
print(p2)
