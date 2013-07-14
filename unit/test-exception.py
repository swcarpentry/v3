import unittest

def in_range(values, low, high):
    if not values:
        raise ValueError, 'no values to search'
    if low >= high:
        raise ValueError, 'illegal range [%f, %f]' % (low, high)
    result = []
    for v in values:
        if low <= v <= high:
            result.append(v)
    return result

# tests:start
class TestInRange(unittest.TestCase):

    def test_no_values(self):
        try:
            in_range([], 0.0, 1.0)
        except ValueError:
            pass
        else:
            self.fail()

    def test_bad_range(self):
        try:
            in_range([0.0], 4.0, -2.0)
        except ValueError:
            pass
        else:
            self.fail()
# tests:end

if __name__ == '__main__':
    unittest.main()
