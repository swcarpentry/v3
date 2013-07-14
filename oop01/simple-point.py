import math

# main:start
class Point(object):

    def set_values(self, x, y):
        self.x = x
        self.y = y

    def get_values(self):
        return (self.x, self.y)

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

if __name__ == '__main__':
    p = Point()
    p.set_values(1.2, 3.5)
    print 'p is', p.get_values()
    print 'norm is', p.norm()
# main:end
