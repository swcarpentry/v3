names = ['goose','tern','tern','hawk','goose','tern', 'goose']
freq = {}
for name in names:
    freq[name] = freq.get(name, 0) + 1

# body:start
keys = freq.keys()
keys.sort()
for k in keys:
    print k, freq[k]
# body:end
