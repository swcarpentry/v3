birthday = {
    'Newton' : 1642,
    'Darwin' : 1809,
    'Turing' : 1912
}

print 'Before deleting Turing:', birthday
del birthday['Turing']
print 'After deleting Turing:', birthday
del birthday['Faraday']
print 'After deleting Faraday:', birthday
