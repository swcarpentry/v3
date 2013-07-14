# Global variable.
rock_type = 'unknown'

# Function that creates local variable.
def classify(rock_name):
    if rock_name in ['basalt', 'granite']:
        rock_type = 'igneous'
    elif rock_name in ['sandstone', 'shale']:
        rock_type = 'sedimentary'
    else:
        rock_type = 'metamorphic'
    print 'in function, rock_type is', rock_type

# Call the function to prove that it uses its local 'x'.
print "before function, rock_type is", rock_type
classify('sandstone')
print "after function, rock_type is", rock_type
