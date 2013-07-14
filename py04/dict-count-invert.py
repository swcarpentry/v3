names = ['goose','tern','tern','hawk','goose','tern', 'goose']
freq = {}
for name in names:
    freq[name] = freq.get(name, 0) + 1

# body:start
inverse = {}
for (key, value) in freq.items():
    seen = inverse.get(value, [])
    seen.append(key)
    inverse[value] = seen

keys = inverse.keys()
keys.sort()
for k in keys:
    print k, inverse[k]
# body:end
