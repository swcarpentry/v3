def circumference(r):
    return 2 * 3.14159 * r

# main:start
def apply_to_list(function, values):
    result = []
    for v in values:
        temp = function(v)
        result.append(temp)
    return result

radii = [0.1, 1.0, 10.0]
print apply_to_list(circumference, radii)
# main:end
