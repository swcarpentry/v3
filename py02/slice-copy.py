metals = ['Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn']
middle = metals[2:-2]
print 'before'
print 'metals:', metals
print 'middle:', middle

middle[0] = 'Al'
del middle[1]

print 'after'
print 'metals:', metals
print 'middle:', middle
