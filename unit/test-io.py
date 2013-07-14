import unittest
from cStringIO import StringIO

def diff(left, right, outstream):
    line_num = 0
    while True:
        left_line = left.readline()
        right_line = right.readline()
        line_num += 1
        if (not left_line) and (not right_line):
            break
        if (not left_line):
            print >> outstream, '<left ends early>'
            break
        if (not right_line):
            print >> outstream, '<right ends early>'
            break
        if left_line != right_line:
            print >> outstream, line_num

# tests:start
class TestDiff(unittest.TestCase):

    def wrap_and_run(self, left, right, expected):
        left = StringIO(left)
        right = StringIO(right)
        actual = StringIO()
        diff(left, right, actual)
        self.assertEqual(actual.getvalue(), expected)

    def test_empty(self):
        self.wrap_and_run('', '', '')

    def test_lengthy_match(self):
        str = '''\
a
b
c
'''
        self.wrap_and_run(str, str, '')

    def test_single_line_mismatch(self):
        self.wrap_and_run('a\n', 'b\n', '1\n')

    def test_middle_mismatch(self):
        self.wrap_and_run('a\nb\nc\n', 'a\nx\nc\n', '2\n')
# tests:end

if __name__ == '__main__':
    unittest.main()
