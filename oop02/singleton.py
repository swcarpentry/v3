# class:start
class AntennaClass(object):
    '''Singleton that controls a radio telescope.'''

    # The unique instance of the class.
    instance = None

    # The constructor fails if an instance already exists.
    def __init__(self, max_rotation):
        assert AntennaClass.instance is None, 'Trying to create a second instance!'
        self.max_rotation = max_rotation
        AntennaClass.instance = self

# Make the creation function look like a class constructor.
def Antenna(max_rotation):
    '''Create and store an AntennaClass instance, or return the one
    that has already been created.'''
    if AntennaClass.instance:
        return AntennaClass.instance
    return AntennaClass(max_rotation)
# class:end

# test:start
first = Antenna(23.5)
print 'first instance:', id(first)
second = Antenna(47.25)
print 'second instance:', id(second)
# test:end
