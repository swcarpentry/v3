import re

dragons = [
    ['CTAGGTGTACTGATG',    'Antipodean Opaleye'],
    ['AAGATGCGTCCGTAT',    'Common Welsh Green'],
    ['AGTCGTGCTCGTTATATC', 'Hebridean Black'],
    ['ATGCGTCGTCGATTATCT', 'Hungarian Horntail'],
    ['CCGTTAGGGCTAAATGCT', 'Norwegian Ridgeback']
]

for (dna, name) in dragons:
    if re.search('ATGCGT', dna):
        print name
