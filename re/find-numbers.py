import re

lines = [
    "Charles Darwin (1809-82)",
    "Darwin's principal works, The Origin of Species (1859)",
    "and The Descent of Man (1871) marked a new epoch in our",
    "understanding of our world and ourselves.  His ideas",
    "were shaped by the Beagle's voyage around the world in",
    "1831-36."
]

for line in lines:
    if re.search('[0-9]+', line):
        print line
