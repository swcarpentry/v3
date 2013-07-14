def is_rock(name):
    return name in ['basalt', 'granite', 'sandstone', 'shale']

if __name__ == '__main__':
    tests = [['basalt', True],  ['gingerale', False],
             [12345678, False], ['sandstone', True]]
    for (value, expected) in tests:
        actual = is_rock(value)
        if actual == expected:
            print 'pass'
        else:
            print 'fail'
