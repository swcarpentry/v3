import unittest

class Molecule(object):

    def __init__(self, **kwargs):
        self.atoms = kwargs

    def __eq__(self, other):
        for k in self.atoms:
            if other.atoms.get(k, -1) != self.atoms[k]:
                return False
        for k in other.atoms:
            if k not in self.atoms:
                return False
        return True

    def __getitem__(self, key):
        return self.atoms[key]

    def erase(self, other):
        for k in other.atoms:
            if k in self.atoms:
                remaining = max(0, self.atoms[k] - other.atoms[k])
                if remaining:
                    self.atoms[k] = remaining
                else:
                    del self.atoms[k]

# tests:start
class TestThiamine(unittest.TestCase):

    def setUp(self):
        self.fixture = Molecule(C=12, H=20, O=1, N=4, S=1)

    def test_erase_nothing(self):
        nothing = Molecule()
        self.fixture.erase(nothing)
        self.assertEqual(self.fixture['C'], 12)
        self.assertEqual(self.fixture['H'], 20)
        self.assertEqual(self.fixture['O'], 1)
        self.assertEqual(self.fixture['N'], 4)
        self.assertEqual(self.fixture['S'], 1)

    def test_erase_single(self):
        self.fixture.erase(Molecule(H=1))
        self.assertEqual(self.fixture, Molecule(C=12, H=19, O=1, N=4, S=1))

    def test_erase_self(self):
        self.fixture.erase(self.fixture)
        self.assertEqual(self.fixture, Molecule())
# tests:end

if __name__ == '__main__':
    unittest.main()
