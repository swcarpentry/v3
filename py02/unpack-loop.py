elements = [
    ['H', 'hydrogen', 1.008],
    ['He', 'helium', 4.003],
    ['Li', 'lithium', 6.941],
    ['Be', 'beryllium', 9.012]
]

for (symbol, name, weight) in elements:
    print name + ' (' + symbol + '): ' + str(weight)
