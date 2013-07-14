# Data to count.
names = ['tern','goose','goose','hawk','tern','goose', 'tern']

# body:start
freq = {}
for name in names:
    freq[name] = freq.get(name, 0) + 1
print freq
# body:end
