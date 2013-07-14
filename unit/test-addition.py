import unittest

class TestAddition(unittest.TestCase):

    def test_zeroes(self):
        self.assertEqual(0 + 0, 0)
        self.assertEqual(5 + 0, 5)
        self.assertEqual(0 + 13.2, 13.2)

    def test_positive(self):
        self.assertEqual(123 + 456, 579)
        self.assertEqual(1.2e20 + 3.4e20, 3.5e20)

    def test_mixed(self):
        self.assertEqual(-19 + 20, 1)
        self.assertEqual(999 + -1, 998)
        self.assertEqual(-300.1 + -400.2, -700.3)

if __name__ == '__main__':
    unittest.main()
