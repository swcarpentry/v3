# builder:start
class AbstractFamily(object):
    '''Builders for particular families derive from this.'''

    def __init__(self, family):
        self.family = family

    def get_name(self):
        return self.name

    def make_controller(self):
        raise NotImplementedError('make_controller missing')

    def make_configuration_panel(self):
        raise NotImplementedError('make_configuration_panel missing')
# builder:end

# manager:start
class FactoryManager(object):
    '''Manage builders by family.'''

    def __init__(self, current_family=None):
        self.builders = {}
        self.family = current_family

    def set_family(self, family):
        assert family, 'Empty family'
        self.family = family

    def add(self, builder):
        name = builder.get_name()
        self.builders[name] = builder

    def make_controller(self):
        self._check_state()
        return self.builders[self.family].make_controller()

    def make_configuration_panel(self):
        self._check_state()
        return self.builders[self.family].make_configuration_panel()

    def _check_state(self):
        assert self.family, 'No family specified'
        assert self.family in self.builders, 'Unknown family:', self.family
# manager:end

# test:start
factory = FactoryManager()
factory.add(RCT100Factory())
factory.add(Subalta4CFactory())
factory.set_family('Subalta4C')
controller = factory.make_controller()
configuration_panel = factory.make_configuration_panel()
# test:end
