import sys, unittest

# main:start
def running_sum(seq):
    result = seq[0:1]
    for i in range(2, len(seq)):
        result.append(result[i-1] + seq[i])
    return result

class SumTests(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(running_sum([]), [])

    def test_single(self):
        self.assertEqual(running_sum([3]), [3])

    def test_double(self):
        self.assertEqual(running_sum([2, 9]), [2, 11])

    def test_long(self):
        self.assertEqual(running_sum([-3, 0, 3, -2, 5]), [-3, -3, 0, -2, 3])
# main:end

if __name__ == '__main__':
    unittest.main()
