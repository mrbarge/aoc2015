import re


def valid1(s):
    i = 0
    found = False
    while i < len(s) - 2 and not found:
        if ord(s[i]) == ord(s[i+1])-1 and ord(s[i]) == ord(s[i+2])-2:
            found = True
        i += 1
    return found


def valid2(s):
    for c in s:
        if c == 'i' or c == 'o' or c == 'l':
            return False
    return True


def valid3(s):
    m = re.findall(r'(.)\1{1,}', s)
    if m:
        allchrs = set(m)
        return len(allchrs) > 1
    else:
        return False


def valid(s):
    return valid1(s) and valid2(s) and valid3(s)


def increment(s):
    ret = ''
    done = False
    for i in range(len(s) - 1, -1, -1):
        if s[i] != 'z' and not done:
            ret = chr(ord(s[i]) + 1) + ret
            done = True
        elif s[i] == 'z' and not done:
            ret = 'a' + ret
        else:
            ret = s[i] + ret
    return ret


def get_next_password(s):
    s = increment(s)
    while not valid(s):
        s = increment(s)
        print(s)
    return s


password = 'vzbxxyzz'
p = get_next_password(password)
print(p)
