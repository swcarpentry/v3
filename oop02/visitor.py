# class:start
class NestedListVisitor(object):
    '''Visit each element in a list of nested lists.'''

    def __init__(self, data):
        '''Construct, but do not run.'''
        assert type(data) is list, 'Only works on lists!'
        self.data = data

    def run(self):
        '''Iterate over all values.'''
        self.recurse(self.data)

    def recurse(self, current):
        '''Loop over a particular list or sub-list (not meant
        to be called by users).'''
        if type(current) is list:
            for v in current:
                self.recurse(v)
        else:
            self.visit(current)

    def visit(self, value):
        '''Users should fill this method in.'''
        pass
# class:end

# test:start
class MaxOfN(NestedListVisitor):

    def __init__(self, data):
        NestedListVisitor.__init__(self, data)
        self.max = None
        self.count = 0

    def visit(self, value):
        self.count += 1
        if self.max is None:
            self.max = value
        else:
            self.max = max(self.max, value)

test_data = [['gold', 'lead'], 'zinc', [['silver', 'iron'], 'mercury']]
test = MaxOfN(test_data)
test.run()
print 'max:', test.max
print 'count:', test.count
# test:end
