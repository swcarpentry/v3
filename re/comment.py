import sys, re

lines = '''Date: 2006-03-07
On duty: HP # 01:30 - 03:00
Observed: Common Welsh Green
On duty: RW #03:00-04:30
Observed: none
On duty: HG # 04:30-06:00
Observed: Hebridean Black
'''.split('\n')

for line in lines:
    match = re.search(r'#\s*(.+)', line)
    if match:
        comment = match.group(1)
        print comment
