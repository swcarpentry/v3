import re

# main:start
tests = [
    ['TTACTA',    True],  # separated by zero G's
    ['TTAGCTA',   True],  # separated by one G
    ['TTAGGGCTA', True],  # separated by three G's
    ['TTAXCTA',   False], # an X in the way
    ['TTAGCGCTA', False], # an embedded X in the way
]

for (dna, expected) in tests:
    actual = re.search('TTAG*CTA', dna) is not None
    assert actual == expected
# main:end
