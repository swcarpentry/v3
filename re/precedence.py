import re

tests = [
    ['ATA',   True],
    ['xATCx', True],
    ['ATG',   False],
    ['AT',    False],
    ['ATAC',  True]
]

for (dna, expected) in tests:
    actual = re.search('AT(A|C)', dna) is not None
    assert actual == expected
