for i in range(4):
    try:
        if (i % 2) == 1:
            raise ValueError('index is odd')
        else:
            print 'not raising exception for %d' % i
    except ValueError, e:
        print 'caught exception for %d' % i, e
