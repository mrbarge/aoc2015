from collections import Counter

def three_vowels(s):
    c = Counter(s)
    num_vowels = c['a'] + c['e'] + c['i'] + c['o'] + c['u']
    if num_vowels >= 3:
        return True
    else:
        return False

def has_doubles(s):
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            return True
        i += 1
    return False

def has_doubles_no_overlap(s):
    i = 0
    while i < len(s)-1:
        j = i+2
        while j < len(s)-1:
            if s[i] == s[j] and s[i+1] == s[j+1]:
                return True
            else:
                j += 1
        i += 1
    return False

def letter_with_gap(s):
    i = 0
    while i < len(s)-2:
        if s[i] == s[i+2]:
            return True
        i += 1
    return False

def no_bad_strings(s):
    if s.find('ab') == s.find('cd') == s.find('pq') == s.find('xy') == -1:
        return True
    else:
        return False

def nice(s):
    if three_vowels(s) and has_doubles(s) and no_bad_strings(s):
        return True
    else:
        return False

def p2nice(s):
    if has_doubles_no_overlap(s) and letter_with_gap(s):
        return True
    else:
        return False

with open('data/day5.input') as f:
    data = [e.strip() for e in f.readlines()]

nice_strings = 0
for line in data:
    if nice(line):
        nice_strings += 1

print(f"Part one: {nice_strings}")

nice_strings = 0
for line in data:
    if p2nice(line):
        nice_strings += 1

print(f"Part two: {nice_strings}")
