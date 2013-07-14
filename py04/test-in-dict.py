birthday = {
    'Newton' : 1642,
    'Darwin' : 1809
}

for name in ['Newton', 'Turing']:
    if name in birthday:
        print name, birthday[name]
    else:
        print 'Who is', name, '?'
