import re

lines = [
    'This has several Title Case words',
    'on Each Line (Some in parentheses).'
]
pattern = re.compile(r'\b([A-Z][a-z]*)\b')
for line in lines:
    print line
    for word in pattern.findall(line):
        print '\t', word
