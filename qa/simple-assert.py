def find_range(values):
    '''Find the non-empty range of values in the input sequence.'''
    assert (type(values) is list) and (len(values) > 0)
    left = min(values)
    right = max(values)
    assert (left in values) and (right in values) and (left <= right)
    return left, right
