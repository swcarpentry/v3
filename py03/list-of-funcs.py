def circumference(r):
    return 2 * 3.14159 * r

# main:start
def area(r):
    return 3.14159 * r * r

def color(r):
    return "unknown"

def apply_each(functions, value):
    result = []
    for f in functions:
        temp = f(value)
        result.append(temp)
    return result

functions = [circumference, area, color]
print apply_each(functions, 1.0)
# main:end
