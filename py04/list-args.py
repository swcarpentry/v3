def sum(*values):
    result = 0.0
    for v in values:
        result += v
    return result

print "no values:", sum()
print "single value:", sum(3)
print "five values:", sum(3, 4, 5, 6, 7)
