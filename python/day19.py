import re

input = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'

def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail

with open('data/day19.input') as f:
    data = [e.strip() for e in f.readlines()]

rules = []
for line in data:
    m = re.match('(.+) => (.+)', line)
    if m:
        rules.append([m[1],m[2]])

unique_combos = set()

for rule in rules:
    matcher = rule[0]
    replacer = rule[1]
    for i in range(0,len(input)):
        if input[i:i+len(matcher)] == matcher:
            replaced = input[:i] + replacer + input[i+len(matcher):]
            unique_combos.add(replaced)

print(f"Part one: {len(unique_combos)}")

# the strategy - try and replace the most specific matches
# as first preference
rules = sorted(rules, key = lambda x: len(x[1]), reverse=True)

target = input
steps = 0
while target != 'e':
    for rule in rules:
        matcher = rule[0]
        replacer = rule[1]
        if replacer in target:
            target = replace_last(target,replacer,matcher)
            steps += 1
    print(target)

print(f"Part two: {steps}")

