import hashlib

secret_key = 'yzbqklnj'

found = False
key_num = 0
while not found:
    m = hashlib.new('md5')
    key = f"{secret_key}{key_num}"
    m.update(str.encode(key))

    md5hash = m.hexdigest()
    if md5hash.startswith('00000'):
        found = True
    else:
        key_num += 1

print(f"Part one: {key_num}")

found = False
key_num = 0
while not found:
    m = hashlib.new('md5')
    key = f"{secret_key}{key_num}"
    m.update(str.encode(key))

    md5hash = m.hexdigest()
    if md5hash.startswith('000000'):
        found = True
    else:
        key_num += 1

print(f"Part two: {key_num}")
