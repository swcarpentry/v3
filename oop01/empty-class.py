# define:start
class Empty(object):
    pass
# define:end

# main:start
if __name__ == '__main__':
    first = Empty()
    second = Empty()
    print 'first has id', id(first)
    print 'second has id', id(second)
# main:end
