# Data to count.
names = ['tern','goose','goose','hawk','tern','goose', 'tern']

# Build a dictionary of frequencies.
freq = {}
for name in names:

    # Already seen, so increment count by one.
    if name in freq:
        freq[name] = freq[name] + 1

    # Never seen before, so add to dictionary.
    else:
        freq[name] = 1

# Display.
print freq
