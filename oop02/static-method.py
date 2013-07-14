class Experiment(object):

    already_done = {}

    @staticmethod
    def get_results(name, *params):
        if name in Experiment.already_done:
            return Experiment.already_done[name]
        exp = Experiment(name, *params)
        exp.run()
        Experiment.already_done[name] = exp
        return exp

    def __init__(self, name, *params):
        self.name = name
        self.params = params

    def run(self):
        pass # would do something in a real program

if __name__ == '__main__':
    first = Experiment.get_results('anti-gravity')
    second = Experiment.get_results('time travel')
    third = Experiment.get_results('anti-gravity')
    print 'first ', id(first)
    print 'second', id(second)
    print 'third ', id(third)
