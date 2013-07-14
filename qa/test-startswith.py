# table:start
Tests = [
    # String  Prefix  Expected
    ['a',     'a',    True],
    ['a',     'b',    False],
    ['abc',   'a',    True],
    ['abc',   'ab',   True],
    ['abc',   'abc',  True],
    ['abc',   'abcd', False],
    ['abc',   '',     True]
]
# table:end

# main:start
passes = 0
failures = 0
for (s, p, expected) in Tests:
    actual = s.startswith(p)
    if actual == expected:
        passes += 1
    else:
        failures += 1
print 'passed', passes, 'out of', passes+failures, 'tests'
# main:end
