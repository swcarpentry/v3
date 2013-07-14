# main:start
class SparseVector(object):
    '''Implement a sparse vector.  If a value has not been set
    explicitly, its value is zero.'''

    def __init__(self):
        '''Construct a sparse vector with all zero entries.'''
        self.data = {}

    def __len__(self):
        '''The length of a vector is one more than the largest index.'''
        if self.data:
            return 1 + max(self.data.keys())
        return 0

    def __getitem__(self, key):
        '''Return an explicit value, or 0.0 if none has been set.'''
        if key in self.data:
            return self.data[key]
        return 0.0

    def __setitem__(self, key, value):
        '''Assign a new value to a vector entry.'''
        if type(key) is not int:
            raise KeyError, 'non-integer index to sparse vector'
        self.data[key] = value
# main:end

# mul:start
    def __mul__(self, other):
        '''Calculate dot product of a sparse vector with something else.'''

        result = 0.0
        for k in self.data:
            result += self.data[k] * other[k]
        return result

    def __rmul__(self, other):
        return self.__mul__(other)
# mul:end

# add:start
    def __add__(self, other):
        '''Add something to a sparse vector.'''

        # Initialize result with all non-zero values from this vector.
        result = SparseVector()
        result.data.update(self.data)

        # If the other object is also a sparse vector, add non-zero values.
        if isinstance(other, SparseVector):
            for k in other.data:
                result[k] = result[k] + other[k]

        # Otherwise, use brute force.
        else:
            for i in range(len(other)):
                result[i] = result[i] + other[i]

        return result

    # Right-hand add does the same thing as left-hand add.
    __radd__ = __add__
# add:end

# str:start
    def __str__(self):
        '''Create printable representation (for testing only).'''
        result = '['
        sep = ''
        for i in range(len(self)):
            result = result + sep + str(self[i])
            sep = ', '
        result += ']'
        return result
# str:end

# tests:start
if __name__ == '__main__':

    x = SparseVector()
    x[1] = 1.0
    x[3] = 3.0
    x[5] = 5.0
    print 'len(x)', len(x)
    for i in range(len(x)):
        print '...', i, x[i]

    y = SparseVector()
    y[1] = 10.0
    y[2] = 20.0
    y[3] = 30.0

    print 'x + y', x + y
    print 'y + x', y + x

    print 'x * y', x * y
    print 'y * x', y * x

    z = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

    print 'x + z', x + z
    print 'x * z', x * z
    print 'z + x', z + x
# tests:end
