birthday = {
    'Newton' : 1642,
    'Darwin' : 1809,
    'Turing' : 1912
}
entry = '\%(name)s: \%(year)s'
for (name, year) in birthday.items():
    temp = {'name' : name, 'year' : year}
    print entry \% temp
