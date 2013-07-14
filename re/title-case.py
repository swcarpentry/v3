import re

# Put pattern outside 'find_all' so that it's only compiled once.
pattern = re.compile(r'\b([A-Z][a-z]*)\b(.*)')

def find_all(line):
    result = []
    match = pattern.search(line)
    while match:
        result.append(match.group(1))
        match = pattern.search(match.group(2))
    return result

lines = [
    'This has several Title Case words',
    'on Each Line (Some in parentheses).'
]
for line in lines:
    print line
    for word in find_all(line):
        print '\t', word
