def format_bits(val, width=1):
    '''Create a base-2 representation of an integer.'''
    result = ''
    while val:
        if val & 0x01:
            result = '1' + result
        else:
            result = '0' + result
        val = val >> 1
    if len(result) < width:
        result = '0' * (width - len(result)) + result
    return result

tests = [
    [ 0, None, '0'],
    [ 0, 4,    '0000'],
    [ 5, None, '101'],
    [19, 8,    '00010011']
]

for (num, width, expected) in tests:
    if width is None:
        actual = format_bits(num)
    else:
        actual = format_bits(num, width)
    print '%4d %8s %10s %10s' % (num, width, expected, actual)
