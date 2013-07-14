from inheritance import Organism, Mammal

# main:start
class Bird(Organism):

    def __init__(self, common_name, sci_name, incubate_period):
        Organism.__init__(self, common_name, sci_name)
        self.incubate_period = incubate_period

    def get_incubate_period(self):
        return self.incubate_period

    def __str__(self):
        extra = ' %d days' % self.incubate_period
        return Organism.__str__(self) + extra

if __name__ == '__main__':
    creatures = [
        Bird('loon', 'gavia immer', 27),
        Mammal('grizzly bear', 'ursus arctos horribilis', 38.0, 210)
    ]
    for c in creatures:
        print c
# main:end
