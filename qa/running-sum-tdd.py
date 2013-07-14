# func:start
def running_sum(vals):
    if type(vals) is not list:
        raise ValueError('non-list as input')
    try:
        result = []
        curr = 0
        for v in vals:
            curr = curr + v
            result.append(curr)
        return result
    except Exception, e:
        raise ValueError('operation error: ' + str(e))
# func:end

# tests:start
Tests = [
    [[],        [],          'empty list'],
    [[1],       [1],         'single value'],
    [[1, 3],    [1, 4],      'two values'],
    [[1, 3, 7], [1, 4, 11],  'three values'],
    [[-1, 1],   [-1, 0],     'negative values'],
    [[1, 3.0],  [1, 4.0],    'mixed types'],
    ["string",  ValueError,  'non-list input'],
    [['a'],     ValueError,  'non-numeric value']
]
# tests:end

passes = failures = errors = 0
for (values, expected, comment) in Tests:

    report = False
    try:
        actual = running_sum(values)
        if actual == expected:
            passes += 1
        else:
            failures += 1
            report = True

    except ValueError:
        if expected is ValueError:
            passes += 1
        else:
            failures += 1
            report = True

    except:
        errors += 1
        report = True

    if report:
        print comment

print 'tests:', passes + failures + errors
print 'passes:', passes
print 'failures:', failures
print 'errors:', errors
