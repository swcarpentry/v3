print 'loading geology module'

def rock_type(rock_name):
    if rock_name in ['basalt', 'granite']:
        return 'igneous'
    elif rock_name in ['sandstone', 'shale']:
        return 'sedimentary'
    else:
        return 'metamorphic'

print 'geology module loaded'
