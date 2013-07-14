def sedimentary(rock_name):
    return rock_name in ['sandstone', 'shale']

sed = sedimentary

print 'original name:', sedimentary.__name__
print 'name of alias:', sed.__name__
