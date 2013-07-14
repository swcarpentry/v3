import re

def reverse_columns(line):
    match = re.search(r'^\s*(\d+)\s+(\d+)\s*$', line)
    if not match:
        return line
    return match.group(2) + ' ' + match.group(1)

tests = [
    ['10 20',    'easy case'],
    [' 30  40 ', 'padding'],
    ['60 70 80', 'too many columns'],
    ['90 end',   'non-numeric']
]

for (fixture, title) in tests:
    actual = reverse_columns(fixture)
    print '%s: "%s" => "%s"' % (title, fixture, actual)
