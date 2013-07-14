# func:start
def total(values, start=0, end=None):

    # If no values given, total is zero.
    if not values:
        return 0

    # If no end specified, use the entire sequence.
    if end is None:
        end = len(values)

    # Calculate.
    result = 0
    for i in range(start, end):
        result += values[i]
    return result
# func:end

# call:start
numbers = [10, 20, 30]
print "numbers being added:", numbers
print "total(numbers, 0, 3):", total(numbers, 0, 3)
print "total(numbers, 2):", total(numbers, 2)
print "total(numbers):", total(numbers)
# call:end
