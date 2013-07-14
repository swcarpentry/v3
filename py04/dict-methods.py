birthday = {
    'Newton' : 1642,
    'Darwin' : 1809,
    'Turing' : 1912
}

print 'keys:', birthday.keys()
print 'values:', birthday.values()
print 'items:', birthday.items()
print 'get:', birthday.get('Curie', 1867)

temp = {
    'Curie'    : 1867,
    'Hopper'   : 1906,
    'Franklin' : 1920
}
birthday.update(temp)
print 'after update:', birthday

birthday.clear()
print 'after clear:', birthday
