from inheritance import Organism, Mammal

# main:start
class Mineral(object):

    def __init__(self, common_name, sci_name, formula):
        self.common_name = common_name
        self.sci_name = sci_name
        self.formula = formula

    def get_common_name(self):
        return self.common_name

    def get_sci_name(self):
        return self.sci_name

    def __str__(self):
        return '%s/%s: %s' % (self.common_name, self.sci_name, self.formula)

if __name__ == '__main__':
    things = [
        Mammal('arctic hare', 'Lepus arcticus', 40.1, 50),
        Mineral("fool's gold", 'iron pyrite', 'FeS2')
    ]
    for t in things:
        print t.get_common_name(), 'is', t.get_sci_name()
# main:end
