names = ['goose','tern','tern','hawk','goose','tern', 'goose']
freq = {}
for name in names:
    freq[name] = freq.get(name, 0) + 1

# body:start
inverse = {}
for (key, value) in freq.items():
    if value not in inverse:
        inverse[value] = []
    inverse[value].append(key)
# body:end

keys = inverse.keys()
keys.sort()
for k in keys:
    print k, inverse[k]
