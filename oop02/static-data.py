class Counter(object):

    num = 0     # Number of Counter objects created.

    def __init__(self, name):
        Counter.num += 1
        self.name = name

if __name__ == '__main__':
    print 'initial count', Counter.num
    first = Counter('first')
    print 'after creating first object', Counter.num
    second = Counter('second')
    print 'after creating second object', Counter.num
