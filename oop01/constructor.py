import math

# main:start
class Point(object):

    def __init__(self, x=0, y=0):
        self.reset(x, y)

    def reset(self, x, y):
        assert (type(x) is int) and (x >= 0), 'x is not non-negative integer'
        assert (type(y) is int) and (y >= 0), 'y is not non-negative integer'
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

if __name__ == '__main__':
    p = Point(1, 1)
    print 'point is initially', p.get()
    p.reset(1, 1)
    print 'p moved to', p.get()
# main:end
