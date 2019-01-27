def run_length(s,i):
    ret = 1
    for i in range(i,len(s)-1):
        if s[i] == s[i+1]:
            ret += 1
        else:
            break
    return ret


def process(s):
    retstr = ''
    i = 0
    while i < len(s):
        rl = run_length(s,i)
        retstr += f"{rl}{s[i]}"
        i += rl
    return retstr


input = '1113222113'

for i in range(0,50):
    input = process(input)

print(f"Part two: {len(input)}")