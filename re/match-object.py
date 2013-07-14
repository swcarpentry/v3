import re

text = 'abbcb'
for pattern in ['b+', 'bc*', 'b+c+']:
    match = re.search(pattern, text)
    print '%s / %s => "%s" (%d, %d)' % \
          (pattern, text, match.group(), match.start(), match.end())
