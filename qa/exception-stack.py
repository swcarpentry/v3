def invert(vals, index):
    try:
        vals[index] = 10.0/vals[index]
    except ArithmeticError, e:
        print 'inner exception handler:', e

def each(vals, indices):
    try:
        for i in indices:
            invert(vals, i)
    except IndexError, e:
        print 'outer exception handler:', e

# Once again, the top index will be out of bounds.
values = [-1, 0, 1]
print 'values before:', values
each(values, range(4))
print 'values after:', values
