Tests = [
    ['a',     'a',    False],    # wrong expected value
    ['a',     1,      False],    # wrong type
    ['abc',   'a',    True]      # everything legal
]

passes = failures = errors = 0
for (s, p, expected) in Tests:
    try:
        actual = s.startswith(p)
        if actual == expected:
            passes += 1
        else:
            failures += 1
    except:
        errors += 1

print 'tests:', passes + failures + errors
print 'passes:', passes
print 'failures:', failures
print 'errors:', errors
