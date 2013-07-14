class Organism(object):

    def __init__(self, common_name, sci_name):
        self.common_name = common_name
        self.sci_name = sci_name

    def get_common_name(self):
        return self.common_name

    def get_sci_name(self):
        return self.sci_name

    def __str__(self):
        return '%s (%s)' % (self.common_name, self.sci_name)

class Mammal(Organism):

    def __init__(self, common_name, sci_name, body_temp, gest_period):
        Organism.__init__(self, common_name, sci_name)
        self.body_temp = body_temp
        self.gest_period = gest_period

    def get_body_temp(self):
        return self.body_temp

    def get_gest_period(self):
        return self.gest_period

    def __str__(self):
        extra = ' %4.2f degrees / %d days' % (self.body_temp, self.gest_period)
        return Organism.__str__(self) + extra

if __name__ == '__main__':
    creature = Mammal('wolf', 'canis lupus', 38.7, 63)
    print creature
